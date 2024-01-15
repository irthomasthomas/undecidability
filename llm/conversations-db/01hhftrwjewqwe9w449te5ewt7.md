**Prompt:**
diff --git a/check-for-change-to-openai-api.sh b/check-for-change-to-openai-api.sh
old mode 100644
new mode 100755
diff --git a/ffmpeg.md b/ffmpeg.md
new file mode 100644
index 0000000..236bdd1
--- /dev/null
+++ b/ffmpeg.md
@@ -0,0 +1,3276 @@
+# FFMPEG {#ffmpeg align="center"}
+
+[NAME](#NAME)\
+[SYNOPSIS](#SYNOPSIS)\
+[DESCRIPTION](#DESCRIPTION)\
+[DETAILED DESCRIPTION](#DETAILED%20DESCRIPTION)\
+[Filtering](#Filtering)\
+[Stream copy](#Stream%20copy)\
+[STREAM SELECTION](#STREAM%20SELECTION)\
+[Description](#Description)\
+[Examples](#Examples)\
+[OPTIONS](#OPTIONS)\
+[Stream specifiers](#Stream%20specifiers)\
+[Generic options](#Generic%20options)\
+[AVOptions](#AVOptions)\
+[Main options](#Main%20options)\
+[Video Options](#Video%20Options)\
+[Advanced Video options](#Advanced%20Video%20options)\
+[Audio Options](#Audio%20Options)\
+[Advanced Audio options](#Advanced%20Audio%20options)\
+[Subtitle options](#Subtitle%20options)\
+[Advanced Subtitle options](#Advanced%20Subtitle%20options)\
+[Advanced options](#Advanced%20options)\
+[Preset files](#Preset%20files)\
+[vstats file format](#vstats%20file%20format)\
+[EXAMPLES](#EXAMPLES)\
+[Video and Audio grabbing](#Video%20and%20Audio%20grabbing)\
+[X11 grabbing](#X11%20grabbing)\
+[Video and Audio file format
+conversion](#Video%20and%20Audio%20file%20format%20conversion)\
+[SEE ALSO](#SEE%20ALSO)\
+[AUTHORS](#AUTHORS)\
+
+------------------------------------------------------------------------
+
+## NAME []{#NAME}
+
+ffmpeg - ffmpeg media converter
+
+## SYNOPSIS []{#SYNOPSIS}
+
+ffmpeg \[*global_options*\] {\[*input_file_options*\] -i *input_url*}
+\... {\[*output_file_options*\] *output_url*} \...
+
+## DESCRIPTION []{#DESCRIPTION}
+
+**ffmpeg** is a universal media converter. It can read a wide variety of
+inputs - including live grabbing/recording devices - filter, and
+transcode them into a plethora of output formats.
+
+**ffmpeg** reads from an arbitrary number of input \"files\" (which can
+be regular files, pipes, network streams, grabbing devices, etc.),
+specified by the \"-i\" option, and writes to an arbitrary number of
+output \"files\", which are specified by a plain output url. Anything
+found on the command line which cannot be interpreted as an option is
+considered to be an output url.
+
+Each input or output url can, in principle, contain any number of
+streams of different types (video/audio/subtitle/attachment/data). The
+allowed number and/or types of streams may be limited by the container
+format. Selecting which streams from which inputs will go into which
+output is either done automatically or with the \"-map\" option (see the
+Stream selection chapter).
+
+To refer to input files in options, you must use their indices
+(0-based). E.g. the first input file is 0, the second is 1, etc.
+Similarly, streams within a file are referred to by their indices. E.g.
+\"2:3\" refers to the fourth stream in the third input file. Also see
+the Stream specifiers chapter.
+
+As a general rule, options are applied to the next specified file.
+Therefore, order is important, and you can have the same option on the
+command line multiple times. Each occurrence is then applied to the next
+input or output file. Exceptions from this rule are the global options
+(e.g. verbosity level), which should be specified first.
+
+Do not mix input and output files \-- first specify all input files,
+then all output files. Also do not mix options which belong to different
+files. All options apply ONLY to the next input or output file and are
+reset between files.
+
+Some simple examples follow.
+
+  -- --- -- ----------------------------------------------------------------------------------
+     •      Convert an input media file to a different format, by re-encoding media streams:
+  -- --- -- ----------------------------------------------------------------------------------
+
+ffmpeg -i input.avi output.mp4
+
+  -- --- -- -------------------------------------------------------- --
+     •      Set the video bitrate of the output file to 64 kbit/s:   
+  -- --- -- -------------------------------------------------------- --
+
+ffmpeg -i input.avi -b:v 64k -bufsize 64k output.mp4
+
+  -- --- -- ---------------------------------------------------- --
+     •      Force the frame rate of the output file to 24 fps:   
+  -- --- -- ---------------------------------------------------- --
+
+ffmpeg -i input.avi -r 24 output.mp4
+
+  -- --- -- -------------------------------------------------------------------------------------------------------------------------------
+     •      Force the frame rate of the input file (valid for raw formats only) to 1 fps and the frame rate of the output file to 24 fps:
+  -- --- -- -------------------------------------------------------------------------------------------------------------------------------
+
+ffmpeg -r 1 -i input.m2v -r 24 output.mp4
+
+The format option may be needed for raw input files.
+
+## DETAILED DESCRIPTION []{#DETAILED DESCRIPTION}
+
+The transcoding process in **ffmpeg** for each output can be described
+by the following diagram:
+
+\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\
+\| \| \| \|\
+\| input \| demuxer \| encoded data \| decoder\
+\| file \| \-\-\-\-\-\-\-\--\> \| packets \| \-\-\-\--+\
+\|\_\_\_\_\_\_\_\| \|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\| \|\
+v\
+\_\_\_\_\_\_\_\_\_\
+\| \|\
+\| decoded \|\
+\| frames \|\
+\|\_\_\_\_\_\_\_\_\_\|\
+\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|\
+\| \| \| \| \|\
+\| output \| \<\-\-\-\-\-\-\-- \| encoded data \| \<\-\-\--+\
+\| file \| muxer \| packets \| encoder\
+\|\_\_\_\_\_\_\_\_\| \|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|
+
+**ffmpeg** calls the libavformat library (containing demuxers) to read
+input files and get packets containing encoded data from them. When
+there are multiple input files, **ffmpeg** tries to keep them
+synchronized by tracking lowest timestamp on any active input stream.
+
+Encoded packets are then passed to the decoder (unless streamcopy is
+selected for the stream, see further for a description). The decoder
+produces uncompressed frames (raw video/PCM audio/\...) which can be
+processed further by filtering (see next section). After filtering, the
+frames are passed to the encoder, which encodes them and outputs encoded
+packets. Finally those are passed to the muxer, which writes the encoded
+packets to the output file.
+
+### Filtering []{#Filtering}
+
+Before encoding, **ffmpeg** can process raw audio and video frames using
+filters from the libavfilter library. Several chained filters form a
+filter graph. **ffmpeg** distinguishes between two types of
+filtergraphs: simple and complex.
+
+*Simple filtergraphs*
+
+Simple filtergraphs are those that have exactly one input and output,
+both of the same type. In the above diagram they can be represented by
+simply inserting an additional step between decoding and encoding:
+
+\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\
+\| \| \| \|\
+\| decoded \| \| encoded data \|\
+\| frames \|\\ \_ \| packets \|\
+\|\_\_\_\_\_\_\_\_\_\| \\ /\|\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\
+\\ \_\_\_\_\_\_\_\_\_\_ /\
+simple \_\\\|\| \| / encoder\
+filtergraph \| filtered \|/\
+\| frames \|\
+\|\_\_\_\_\_\_\_\_\_\_\|
+
+Simple filtergraphs are configured with the per-stream **-filter**
+option (with **-vf** and **-af** aliases for video and audio
+respectively). A simple filtergraph for video can look for example like
+this:
+
+\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_
+\_\_\_\_\_\_\_\_\
+\| \| \| \| \| \| \| \|\
+\| input \| \-\--\> \| deinterlace \| \-\--\> \| scale \| \-\--\> \|
+output \|\
+\|\_\_\_\_\_\_\_\| \|\_\_\_\_\_\_\_\_\_\_\_\_\_\| \|\_\_\_\_\_\_\_\|
+\|\_\_\_\_\_\_\_\_\|
+
+Note that some filters change frame properties but not frame contents.
+E.g. the \"fps\" filter in the example above changes number of frames,
+but does not touch the frame contents. Another example is the \"setpts\"
+filter, which only sets timestamps and otherwise passes the frames
+unchanged.
+
+*Complex filtergraphs*
+
+Complex filtergraphs are those which cannot be described as simply a
+linear processing chain applied to one stream. This is the case, for
+example, when the graph has more than one input and/or output, or when
+output stream type is different from input. They can be represented with
+the following diagram:
+
+\_\_\_\_\_\_\_\_\_\
+\| \|\
+\| input 0 \|\\ \_\_\_\_\_\_\_\_\_\_\
+\|\_\_\_\_\_\_\_\_\_\| \\ \| \|\
+\\ \_\_\_\_\_\_\_\_\_ /\| output 0 \|\
+\\ \| \| / \|\_\_\_\_\_\_\_\_\_\_\|\
+\_\_\_\_\_\_\_\_\_ \\\| complex \| /\
+\| \| \| \|/\
+\| input 1 \|\-\-\--\>\| filter \|\\\
+\|\_\_\_\_\_\_\_\_\_\| \| \| \\ \_\_\_\_\_\_\_\_\_\_\
+/\| graph \| \\ \| \|\
+/ \| \| \\\| output 1 \|\
+\_\_\_\_\_\_\_\_\_ / \|\_\_\_\_\_\_\_\_\_\| \|\_\_\_\_\_\_\_\_\_\_\|\
+\| \| /\
+\| input 2 \|/\
+\|\_\_\_\_\_\_\_\_\_\|
+
+Complex filtergraphs are configured with the **-filter_complex** option.
+Note that this option is global, since a complex filtergraph, by its
+nature, cannot be unambiguously associated with a single stream or file.
+
+The **-lavfi** option is equivalent to **-filter_complex**.
+
+A trivial example of a complex filtergraph is the \"overlay\" filter,
+which has two video inputs and one video output, containing one video
+overlaid on top of the other. Its audio counterpart is the \"amix\"
+filter.
+
+### Stream copy []{#Stream copy}
+
+Stream copy is a mode selected by supplying the \"copy\" parameter to
+the **-codec** option. It makes **ffmpeg** omit the decoding and
+encoding step for the specified stream, so it does only demuxing and
+muxing. It is useful for changing the container format or modifying
+container-level metadata. The diagram above will, in this case, simplify
+to this:
+
+\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\
+\| \| \| \| \| \|\
+\| input \| demuxer \| encoded data \| muxer \| output \|\
+\| file \| \-\-\-\-\-\-\-\--\> \| packets \| \-\-\-\-\-\--\> \| file \|\
+\|\_\_\_\_\_\_\_\| \|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\| \|\_\_\_\_\_\_\_\_\|
+
+Since there is no decoding or encoding, it is very fast and there is no
+quality loss. However, it might not work in some cases because of many
+factors. Applying filters is obviously also impossible, since filters
+work on uncompressed data.
+
+## STREAM SELECTION []{#STREAM SELECTION}
+
+**ffmpeg** provides the \"-map\" option for manual control of stream
+selection in each output file. Users can skip \"-map\" and let ffmpeg
+perform automatic stream selection as described below. The \"-vn / -an /
+-sn / -dn\" options can be used to skip inclusion of video, audio,
+subtitle and data streams respectively, whether manually mapped or
+automatically selected, except for those streams which are outputs of
+complex filtergraphs.
+
+### Description []{#Description}
+
+The sub-sections that follow describe the various rules that are
+involved in stream selection. The examples that follow next show how
+these rules


**Response:**
Add ffmpeg.md to project directory.

<details><summary>Metadata</summary>

- Duration: 1380 ms
- Datetime: 2023-12-12T20:16:24.809619
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

