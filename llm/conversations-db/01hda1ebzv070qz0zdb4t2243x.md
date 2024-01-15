**Prompt:**
import cv2
import numpy as np
import click


class LightningDetector:
    def __init__(self, video_file, brightness_threshold=80, motion_threshold=10000):
        self.video_file = video_file
        self.brightness_threshold = brightness_threshold
        self.motion_threshold = motion_threshold

    def calculate_brightness(self, current_frame, previous_frame):
        difference = cv2.absdiff(current_frame, previous_frame)
        brightness_diff = np.sum(difference)
        return brightness_diff

    def calculate_motion(self, prvs, next, show_motion=False):
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])

        if show_motion:
            hsv = np.zeros_like(prvs)
            hsv[..., 1] = 255
            hsv[..., 0] = ang * 180 / np.pi / 2
            hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            cv2.imshow('Motion Vis', rgb)
            cv2.waitKey(1)  # Adds a small delay and also allows input, use it to quit the window
        return np.sum(mag)

    def detect_lightning(self, show_motion=False):
        cap = cv2.VideoCapture(self.video_file)

        frame_rate = cap.get(5)  # get frame rate
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        # Prepare video writer
        fourcc = -1  # This could make the system request the specific codec
        params = [
            cv2.VIDEOWRITER_PROP_HW_ACCELERATION,
            cv2.VIDEOWRITER_PROP_HW_DEVICE,
            0,  # Change it according to your preferred device
        ]
        out = cv2.VideoWriter('lightning_output.avi', fourcc, frame_rate, (frame_width, frame_height))

        num_frames = 0
        previous_frame = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            num_frames += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if num_frames == 1:
                previous_frame = gray.copy()
                continue

            brightness_diff = self.calculate_brightness(gray, previous_frame)
            motion = self.calculate_motion(previous_frame, gray, show_motion)

            if brightness_diff > self.brightness_threshold or motion > self.motion_threshold:
                out.write(frame)

            previous_frame = gray.copy()

        cap.release()
        out.release()
        cv2.destroyAllWindows()

@click.command()
@click.option('--video_file', type=click.Path(exists=True), required=True, help='Path to your video file.')
@click.option('--brightness_threshold', type=int, default=80, help='Brightness threshold value.')
@click.option('--motion_threshold', type=int, default=10000, help='Motion threshold value.')
@click.option('--show_motion', is_flag=True, default=False, help='Show motion or not.')

def main(video_file, brightness_threshold, motion_threshold, show_motion):
    ld = LightningDetector(video_file, brightness_threshold, motion_threshold)
    ld.detect_lightning(show_motion)


if __name__ == "__main__":
    main()

OpenCV: FFMPEG: format avi / AVI (Audio Video Interleaved)
fourcc tag 0x34363248/'H264' codec_id 001B
fourcc tag 0x34363268/'h264' codec_id 001B
fourcc tag 0x34363258/'X264' codec_id 001B
fourcc tag 0x34363278/'x264' codec_id 001B
fourcc tag 0x31637661/'avc1' codec_id 001B
fourcc tag 0x43564144/'DAVC' codec_id 001B
fourcc tag 0x32564d53/'SMV2' codec_id 001B
fourcc tag 0x48535356/'VSSH' codec_id 001B
fourcc tag 0x34363251/'Q264' codec_id 001B
fourcc tag 0x34363256/'V264' codec_id 001B
fourcc tag 0x43564147/'GAVC' codec_id 001B
fourcc tag 0x56534d55/'UMSV' codec_id 001B
fourcc tag 0x64687374/'tshd' codec_id 001B
fourcc tag 0x434d4e49/'INMC' codec_id 001B
fourcc tag 0x33363248/'H263' codec_id 0004
fourcc tag 0x33363258/'X263' codec_id 0004
fourcc tag 0x33363254/'T263' codec_id 0004
fourcc tag 0x3336324c/'L263' codec_id 0004
fourcc tag 0x4b315856/'VX1K' codec_id 0004
fourcc tag 0x6f47795a/'ZyGo' codec_id 0004
fourcc tag 0x3336324d/'M263' codec_id 0004
fourcc tag 0x6d76736c/'lsvm' codec_id 0004
fourcc tag 0x33363248/'H263' codec_id 0013
fourcc tag 0x33363249/'I263' codec_id 0014
fourcc tag 0x31363248/'H261' codec_id 0003
fourcc tag 0x33363255/'U263' codec_id 0004
fourcc tag 0x344d5356/'VSM4' codec_id 0004
fourcc tag 0x34504d46/'FMP4' codec_id 000C
fourcc tag 0x58564944/'DIVX' codec_id 000C
fourcc tag 0x30355844/'DX50' codec_id 000C
fourcc tag 0x44495658/'XVID' codec_id 000C
fourcc tag 0x5334504d/'MP4S' codec_id 000C
fourcc tag 0x3253344d/'M4S2' codec_id 000C
fourcc tag 0x00000004/'????' codec_id 000C
fourcc tag 0x34504d5a/'ZMP4' codec_id 000C
fourcc tag 0x31564944/'DIV1' codec_id 000C
fourcc tag 0x305a4c42/'BLZ0' codec_id 000C
fourcc tag 0x7634706d/'mp4v' codec_id 000C
fourcc tag 0x34504d55/'UMP4' codec_id 000C
fourcc tag 0x46315657/'WV1F' codec_id 000C
fourcc tag 0x47444553/'SEDG' codec_id 000C
fourcc tag 0x34504d52/'RMP4' codec_id 000C
fourcc tag 0x32564933/'3IV2' codec_id 000C
fourcc tag 0x56574157/'WAWV' codec_id 000C
fourcc tag 0x53444646/'FFDS' codec_id 000C
fourcc tag 0x57465646/'FVFW' codec_id 000C
fourcc tag 0x444f4344/'DCOD' codec_id 000C
fourcc tag 0x4d58564d/'MVXM' codec_id 000C
fourcc tag 0x56344d50/'PM4V' codec_id 000C
fourcc tag 0x34504d53/'SMP4' codec_id 000C
fourcc tag 0x4d475844/'DXGM' codec_id 000C
fourcc tag 0x4d444956/'VIDM' codec_id 000C
fourcc tag 0x3354344d/'M4T3' codec_id 000C
fourcc tag 0x584f4547/'GEOX' codec_id 000C
fourcc tag 0x34363247/'G264' codec_id 000C
fourcc tag 0x34584448/'HDX4' codec_id 000C
fourcc tag 0x56344d44/'DM4V' codec_id 000C
fourcc tag 0x324b4d44/'DMK2' codec_id 000C
fourcc tag 0x344d5944/'DYM4' codec_id 000C
fourcc tag 0x49474944/'DIGI' codec_id 000C
fourcc tag 0x56485045/'EPHV' codec_id 000C
fourcc tag 0x41344d45/'EM4A' codec_id 000C
fourcc tag 0x4343344d/'M4CC' codec_id 000C
fourcc tag 0x30344e53/'SN40' codec_id 000C
fourcc tag 0x58505356/'VSPX' codec_id 000C
fourcc tag 0x58444c55/'ULDX' codec_id 000C
fourcc tag 0x564f4547/'GEOV' codec_id 000C
fourcc tag 0x50504953/'SIPP' codec_id 000C
fourcc tag 0x56344d53/'SM4V' codec_id 000C
fourcc tag 0x58495658/'XVIX' codec_id 000C
fourcc tag 0x58657244/'DreX' codec_id 000C
fourcc tag 0x34504d51/'QMP4' codec_id 000C
fourcc tag 0x31564c50/'PLV1' codec_id 000C
fourcc tag 0x34564c47/'GLV4' codec_id 000C
fourcc tag 0x34504d47/'GMP4' codec_id 000C
fourcc tag 0x344d4e4d/'MNM4' codec_id 000C
fourcc tag 0x344d5447/'GTM4' codec_id 000C
fourcc tag 0x3334504d/'MP43' codec_id 0010
fourcc tag 0x33564944/'DIV3' codec_id 0010
fourcc tag 0x3347504d/'MPG3' codec_id 0010
fourcc tag 0x35564944/'DIV5' codec_id 0010
fourcc tag 0x36564944/'DIV6' codec_id 0010
fourcc tag 0x34564944/'DIV4' codec_id 0010
fourcc tag 0x33585644/'DVX3' codec_id 0010
fourcc tag 0x31345041/'AP41' codec_id 0010
fourcc tag 0x314c4f43/'COL1' codec_id 0010
fourcc tag 0x304c4f43/'COL0' codec_id 0010
fourcc tag 0x3234504d/'MP42' codec_id 000F
fourcc tag 0x32564944/'DIV2' codec_id 000F
fourcc tag 0x3447504d/'MPG4' codec_id 000E
fourcc tag 0x3134504d/'MP41' codec_id 000E
fourcc tag 0x31564d57/'WMV1' codec_id 0011
fourcc tag 0x32564d57/'WMV2' codec_id 0012
fourcc tag 0x45565847/'GXVE' codec_id 0012
fourcc tag 0x64737664/'dvsd' codec_id 0018
fourcc tag 0x64687664/'dvhd' codec_id 0018
fourcc tag 0x31687664/'dvh1' codec_id 0018
fourcc tag 0x6c737664/'dvsl' codec_id 0018
fourcc tag 0x35327664/'dv25' codec_id 0018
fourcc tag 0x30357664/'dv50' codec_id 0018
fourcc tag 0x63766463/'cdvc' codec_id 0018
fourcc tag 0x48564443/'CDVH' codec_id 0018
fourcc tag 0x35564443/'CDV5' codec_id 0018
fourcc tag 0x20637664/'dvc ' codec_id 0018
fourcc tag 0x73637664/'dvcs' codec_id 0018
fourcc tag 0x31687664/'dvh1' codec_id 0018
fourcc tag 0x73697664/'dvis' codec_id 0018
fourcc tag 0x63766470/'pdvc' codec_id 0018
fourcc tag 0x35324c53/'SL25' codec_id 0018
fourcc tag 0x56444c53/'SLDV' codec_id 0018
fourcc tag 0x31645641/'AVd1' codec_id 0018
fourcc tag 0x3167706d/'mpg1' codec_id 0001
fourcc tag 0x3267706d/'mpg2' codec_id 0002
fourcc tag 0x4745504d/'MPEG' codec_id 0002
fourcc tag 0x314d4950/'PIM1' codec_id 0001
fourcc tag 0x324d4950/'PIM2' codec_id 0002
fourcc tag 0x32524356/'VCR2' codec_id 0001
fourcc tag 0x10000001/'????' codec_id 0001
fourcc tag 0x10000002/'????' codec_id 0002
fourcc tag 0x10000004/'????' codec_id 000C
fourcc tag 0x20525644/'DVR ' codec_id 0002
fourcc tag 0x53454d4d/'MMES' codec_id 0002
fourcc tag 0x32504d4c/'LMP2' codec_id 0002
fourcc tag 0x66696c73/'slif' codec_id 0002
fourcc tag 0x56324d45/'EM2V' codec_id 0002
fourcc tag 0x3130374d/'M701' codec_id 0002
fourcc tag 0x3230374d/'M702' codec_id 0002
fourcc tag 0x3330374d/'M703' codec_id 0002
fourcc tag 0x3430374d/'M704' codec_id 0002
fourcc tag 0x3530374d/'M705' codec_id 0002
fourcc tag 0x7667706d/'mpgv' codec_id 0002
fourcc tag 0x30315742/'BW10' codec_id 0001
fourcc tag 0x47504d58/'XMPG' codec_id 0001
fourcc tag 0x47504a4d/'MJPG' codec_id 0007
fourcc tag 0x3243534d/'MSC2' codec_id 0007
fourcc tag 0x47504a4c/'LJPG' codec_id 0007
fourcc tag 0x31626d64/'dmb1' codec_id 0007
fourcc tag 0x61706a6d/'mjpa' codec_id 0007
fourcc tag 0x3432524a/'JR24' codec_id 0007
fourcc tag 0x47504a4c/'LJPG' codec_id 0009
fourcc tag 0x4c47504a/'JPGL' codec_id 0007
fourcc tag 0x534c4a4d/'MJLS' codec_id 000B
fourcc tag 0x47504a4d/'MJPG' codec_id 000B
fourcc tag 0x534c4a4d/'MJLS' codec_id 0007
fourcc tag 0x6765706a/'jpeg' codec_id 0007
fourcc tag 0x47504a49/'IJPG' codec_id 0007
fourcc tag 0x6e525641/'AVRn' codec_id 00CE
fourcc tag 0x56444341/'ACDV' codec_id 0007
fourcc tag 0x47564951/'QIVG' codec_id 0007
fourcc tag 0x4a4d4c53/'SLMJ' codec_id 0007
fourcc tag 0x47504a43/'CJPG' codec_id 0007
fourcc tag 0x564c4a49/'IJLV' codec_id 0007
fourcc tag 0x504a564d/'MVJP' codec_id 0007
fourcc tag 0x31495641/'AVI1' codec_id 0007
fourcc tag 0x32495641/'AVI2' codec_id 0007
fourcc tag 0x4a53544d/'MTSJ' codec_id 0007
fourcc tag 0x47504a5a/'ZJPG' codec_id 0007
fourcc tag 0x504a4d4d/'MMJP' codec_id 0007
fourcc tag 0x55594648/'HFYU' codec_id 0019
fourcc tag 0x48564646/'FFVH' codec_id 0043
fourcc tag 0x56555943/'CYUV' codec_id 001A
fourcc tag 0x00000000/'????' codec_id 000D
fourcc tag 0x00000003/'????' codec_id 000D
fourcc tag 0x30323449/'I420' codec_id 000D
fourcc tag 0x32595559/'YUY2' codec_id 000D
fourcc tag 0x32323459/'Y422' codec_id 000D
fourcc tag 0x32323456/'V422' codec_id 000D
fourcc tag 0x564e5559/'YUNV' codec_id 000D
fourcc tag 0x564e5955/'UYNV' codec_id 000D
fourcc tag 0x594e5955/'UYNY' codec_id 000D
fourcc tag 0x31767975/'uyv1' codec_id 000D
fourcc tag 0x31755632/'2Vu1' codec_id 000D
fourcc tag 0x79757632/'2vuy' codec_id 000D
fourcc tag 0x73767579/'yuvs' codec_id 000D
fourcc tag 0x32767579/'yuv2' codec_id 000D
fourcc tag 0x32323450/'P422' codec_id 000D
fourcc tag 0x32315659/'YV12' codec_id 000D
fourcc tag 0x36315659/'YV16' codec_id 000D
fourcc tag 0x34325659/'YV24' codec_id 000D
fourcc tag 0x59565955/'UYVY' codec_id 000D
fourcc tag 0x59555956/'VYUY' codec_id 000D
fourcc tag 0x56555949/'IYUV' codec_id 000D
fourcc tag 0x30303859/'Y800' codec_id 000D
fourcc tag 0x20203859/'Y8  ' codec_id 000D
fourcc tag 0x43594448/'HDYC' codec_id 000D
fourcc tag 0x39555659/'YVU9' codec_id 000D
fourcc tag 0x5a544456/'VDTZ' codec_id 000D
fourcc tag 0x31313459/'Y411' codec_id 000D
fourcc tag 0x3231564e/'NV12' codec_id 000D
fourcc tag 0x3132564e/'NV21' codec_id 000D
fourcc tag 0x42313459/'Y41B' codec_id 000D
fourcc tag 0x42323459/'Y42B' codec_id 000D
fourcc tag 0x39565559/'YUV9' codec_id 000D
fourcc tag 0x39555659/'YVU9' codec_id 000D
fourcc tag 0x32767561/'auv2' codec_id 000D
fourcc tag 0x55595659/'YVYU' codec_id 000D
fourcc tag 0x56595559/'YUYV' codec_id 000D
fourcc tag 0x30313449/'I410' codec_id 000D
fourcc tag 0x31313449/'I411' codec_id 000D
fourcc tag 0x32323449/'I422' codec_id 000D
fourcc tag 0x30343449/'I440' codec_id 000D
fourcc tag 0x34343449/'I444' codec_id 000D
fourcc tag 0x3032344a/'J420' codec_id 000D
fourcc tag 0x3232344a/'J422' codec_id 000D
fourcc tag 0x3034344a/'J440' codec_id 000D
fourcc tag 0x3434344a/'J444' codec_id 000D
fourcc tag 0x41565559/'YUVA' codec_id 000D
fourcc tag 0x41303449/'I40A' codec_id 000D
fourcc tag 0x41323449/'I42A' codec_id 000D
fourcc tag 0x32424752/'RGB2' codec_id 000D
fourcc tag 0x35315652/'RV15' codec_id 000D
fourcc tag 0x36315652/'RV16' codec_id 000D
fourcc tag 0x34325652/'RV24' codec_id 000D
fourcc tag 0x32335652/'RV32' codec_id 000D
fourcc tag 0x41424752/'RGBA' codec_id 000D
fourcc tag 0x32335641/'AV32' codec_id 000D
fourcc tag 0x59455247/'GREY' codec_id 000D
fourcc tag 0x4c393049/'I09L' codec_id 000D
fourcc tag 0x42393049/'I09B' codec_id 000D
fourcc tag 0x4c393249/'I29L' codec_id 000D
fourcc tag 0x42393249/'I29B' codec_id 000D
fourcc tag 0x4c393449/'I49L' codec_id 000D
fourcc tag 0x42393449/'I49B' codec_id 000D
fourcc tag 0x4c413049/'I0AL' codec_id 000D
fourcc tag 0x42413049/'I0AB' codec_id 000D
fourcc tag 0x4c413249/'I2AL' codec_id 000D
fourcc tag 0x42413249/'I2AB' codec_id 000D
fourcc tag 0x4c413449/'I4AL' codec_id 000D
fourcc tag 0x42413449/'I4AB' codec_id 000D
fourcc tag 0x4c463449/'I4FL' codec_id 000D
fourcc tag 0x42463449/'I4FB' codec_id 000D
fourcc tag 0x4c433049/'I0CL' codec_id 000D
fourcc tag 0x42433049/'I0CB' codec_id 000D
fourcc tag 0x4c433249/'I2CL' codec_id 000D
fourcc tag 0x42433249/'I2CB' codec_id 000D
fourcc tag 0x4c433449/'I4CL' codec_id 000D
fourcc tag 0x42433449/'I4CB' codec_id 000D
fourcc tag 0x4c463049/'I0FL' codec_id 000D
fourcc tag 0x42463049/'I0FB' codec_id 000D
fourcc tag 0x55575246/'FRWU' codec_id 0082
fourcc tag 0x6b303152/'R10k' codec_id 0090
fourcc tag 0x30313272/'r210' codec_id 0085
fourcc tag 0x30313276/'v210' codec_id 007F
fourcc tag 0x30313243/'C210' codec_id 007F
fourcc tag 0x38303376/'v308' codec_id 00CB
fourcc tag 0x38303476/'v408' codec_id 00CC
fourcc tag 0x56555941/'AYUV' codec_id 00C9
fourcc tag 0x30313476/'v410' codec_id 009C
fourcc tag 0x34767579/'yuv4' codec_id 00CD
fourcc tag 0x31335649/'IV31' codec_id 001C
fourcc tag 0x32335649/'IV32' codec_id 001C
fourcc tag 0x31345649/'IV41' codec_id 006F
fourcc tag 0x30355649/'IV50' codec_id 0070
fourcc tag 0x31335056/'VP31' codec_id 001D
fourcc tag 0x30335056/'VP30' codec_id 001D
fourcc tag 0x30345056/'VP40' codec_id 00F2
fourcc tag 0x30355056/'VP50' codec_id 005A
fourcc tag 0x30365056/'VP60' codec_id 005B
fourcc tag 0x31365056/'VP61' codec_id 005B
fourcc tag 0x32365056/'VP62' codec_id 005B
fourcc tag 0x41365056/'VP6A' codec_id 006A
fourcc tag 0x46365056/'VP6F' codec_id 005C
fourcc tag 0x34564c46/'FLV4' codec_id 005C
fourcc tag 0x30375056/'VP70' codec_id 00B3
fourcc tag 0x31375056/'VP71' codec_id 00B3
fourcc tag 0x30385056/'VP80' codec_id 008B
fourcc tag 0x30395056/'VP90' codec_id 00A7
fourcc tag 0x31565341/'ASV1' codec_id 001F
fourcc tag 0x32565341/'ASV2' codec_id 0020
fourcc tag 0x31524356/'VCR1' codec_id 0023
fourcc tag 0x31564646/'FFV1' codec_id 0021
fourcc tag 0x6e617858/'Xxan' codec_id 0029
fourcc tag 0x30324d4c/'LM20' codec_id 0071
fourcc tag 0x656c726d/'mrle' codec_id 002D
fourcc tag 0x00000001/'????' codec_id 002D
fourcc tag 0x00000002/'????' codec_id 002D
fourcc tag 0x4356534d/'MSVC' codec_id 002E
fourcc tag 0x6376736d/'msvc' codec_id 002E
fourcc tag 0x4d415243/'CRAM' codec_id 002E
fourcc tag 0x6d617263/'cram' codec_id 002E
fourcc tag 0x4d414857/'WHAM' codec_id 002E
fourcc tag 0x6d616877/'wham' codec_id 002E
fourcc tag 0x64697663/'cvid' codec_id 002B
fourcc tag 0x4b435544/'DUCK' codec_id 0033
fourcc tag 0x5a455650/'PVEZ' codec_id 0033
fourcc tag 0x485a534d/'MSZH' codec_id 0035
fourcc tag 0x42494c5a/'ZLIB' codec_id 0036
fourcc tag 0x574f4e53/'SNOW' codec_id 00D1
fourcc tag 0x564d5834/'4XMV' codec_id 0022
fourcc tag 0x31564c46/'FLV1' codec_id 0015
fourcc tag 0x33363253/'S263' codec_id 0015
fourcc tag 0x31565346/'FSV1' codec_id 0056
fourcc tag 0x31717673/'svq1' codec_id 0016
fourcc tag 0x63637374/'tscc' codec_id 0038
fourcc tag 0x49544c55/'ULTI' codec_id 0039
fourcc tag 0x4c584956/'VIXL' codec_id 003B
fourcc tag 0x47455051/'QPEG' codec_id 003C
fourcc tag 0x302e3151/'Q1.0' codec_id 003C
fourcc tag 0x312e3151/'Q1.1' codec_id 003C
fourcc tag 0x33564d57/'WMV3' codec_id 0047
fourcc tag 0x50564d57/'WMVP' codec_id 0096
fourcc tag 0x31435657/'WVC1' codec_id 0046
fourcc tag 0x41564d57/'WMVA' codec_id 0046
fourcc tag 0x32505657/'WVP2' codec_id 0097
fourcc tag 0x4f434f4c/'LOCO' codec_id 0048
fourcc tag 0x31564e57/'WNV1' codec_id 0049
fourcc tag 0x38565559/'YUV8' codec_id 0049
fourcc tag 0x34534141/'AAS4' codec_id 004A
fourcc tag 0x43534141/'AASC' codec_id 004A
fourcc tag 0x31325452/'RT21' codec_id 004B
fourcc tag 0x31535046/'FPS1' codec_id 004C
fourcc tag 0x6f656874/'theo' codec_id 001E
fourcc tag 0x30324d54/'TM20' codec_id 004D
fourcc tag 0x30325254/'TR20' codec_id 00D6
fourcc tag 0x44435343/'CSCD' codec_id 004F
fourcc tag 0x56424d5a/'ZMBV' codec_id 0051
fourcc tag 0x43564d4b/'KMVC' codec_id 0055
fourcc tag 0x53564143/'CAVS' codec_id 0057
fourcc tag 0x32535641/'AVS2' codec_id 00C0
fourcc tag 0x32706a6d/'mjp2' codec_id 0058
fourcc tag 0x43324a4d/'MJ2C' codec_id 0058
fourcc tag 0x43324a4c/'LJ2C' codec_id 0058
fourcc tag 0x4b324a4c/'LJ2K' codec_id 0058
fourcc tag 0x324a5049/'IPJ2' codec_id 0058
fourcc tag 0x326a5641/'AVj2' codec_id 0058
fourcc tag 0x636e4d56/'VMnc' codec_id 0059
fourcc tag 0x20616774/'tga ' codec_id 005D
fourcc tag 0x474e504d/'MPNG' codec_id 003D
fourcc tag 0x31474e50/'PNG1' codec_id 003D
fourcc tag 0x20676e70/'png ' codec_id 003D
fourcc tag 0x524a4c43/'CLJR' codec_id 0024
fourcc tag 0x63617264/'drac' codec_id 0074
fourcc tag 0x72707a61/'azpr' codec_id 002A
fourcc tag 0x415a5052/'RPZA' codec_id 002A
fourcc tag 0x617a7072/'rpza' codec_id 002A
fourcc tag 0x34355053/'SP54' codec_id 000A
fourcc tag 0x41525541/'AURA' codec_id 007B
fourcc tag 0x32525541/'AUR2' codec_id 007C
fourcc tag 0x20787064/'dpx ' codec_id 0080
fourcc tag 0x3156474b/'KGV1' codec_id 0089
fourcc tag 0x5347414c/'LAGS' codec_id 0092
fourcc tag 0x46564d41/'AMVF' codec_id 006B
fourcc tag 0x41524c55/'ULRA' codec_id 0098
fourcc tag 0x47524c55/'ULRG' codec_id 0098
fourcc tag 0x30594c55/'ULY0' codec_id 0098
fourcc tag 0x32594c55/'ULY2' codec_id 0098
fourcc tag 0x34594c55/'ULY4' codec_id 0098
fourcc tag 0x30484c55/'ULH0' codec_id 0098
fourcc tag 0x32484c55/'ULH2' codec_id 0098
fourcc tag 0x34484c55/'ULH4' codec_id 0098
fourcc tag 0x30595155/'UQY0' codec_id 0098
fourcc tag 0x32595155/'UQY2' codec_id 0098
fourcc tag 0x41525155/'UQRA' codec_id 0098
fourcc tag 0x47525155/'UQRG' codec_id 0098
fourcc tag 0x32594d55/'UMY2' codec_id 0098
fourcc tag 0x32484d55/'UMH2' codec_id 0098
fourcc tag 0x34594d55/'UMY4' codec_id 0098
fourcc tag 0x34484d55/'UMH4' codec_id 0098
fourcc tag 0x41524d55/'UMRA' codec_id 0098
fourcc tag 0x47524d55/'UMRG' codec_id 0098
fourcc tag 0x454c4256/'VBLE' codec_id 009A
fourcc tag 0x30333145/'E130' codec_id 00A9
fourcc tag 0x726f7478/'xtor' codec_id 009B
fourcc tag 0x4f43455a/'ZECO' codec_id 00A0
fourcc tag 0x50313459/'Y41P' codec_id 00C5
fourcc tag 0x434c4641/'AFLC' codec_id 0032
fourcc tag 0x3153534d/'MSS1' codec_id 00A1
fourcc tag 0x3141534d/'MSA1' codec_id 00A2
fourcc tag 0x32435354/'TSC2' codec_id 00A3
fourcc tag 0x3253544d/'MTS2' codec_id 00A4
fourcc tag 0x434c4c43/'CLLC' codec_id 00A5
fourcc tag 0x3253534d/'MSS2' codec_id 00A6
fourcc tag 0x33515653/'SVQ3' codec_id 0017
fourcc tag 0x76323130/'012v' codec_id 00C7
fourcc tag 0x76323161/'a12v' codec_id 00C7
fourcc tag 0x324d3247/'G2M2' codec_id 00AA
fourcc tag 0x334d3247/'G2M3' codec_id 00AA
fourcc tag 0x344d3247/'G2M4' codec_id 00AA
fourcc tag 0x354d3247/'G2M5' codec_id 00AA
fourcc tag 0x56434946/'FICV' codec_id 00AE
fourcc tag 0x58514843/'CHQX' codec_id 00B8
fourcc tag 0x43534454/'TDSC' codec_id 00B9
fourcc tag 0x43565543/'CUVC' codec_id 00BA
fourcc tag 0x30345652/'RV40' codec_id 0045
fourcc tag 0x31565053/'SPV1' codec_id 00BE
fourcc tag 0x43435352/'RSCC' codec_id 00BF
fourcc tag 0x43435349/'ISCC' codec_id 00BF
fourcc tag 0x44484643/'CFHD' codec_id 00D5
fourcc tag 0x3130314d/'M101' codec_id 00D7
fourcc tag 0x3230314d/'M102' codec_id 00D7
fourcc tag 0x5947414d/'MAGY' codec_id 00D8
fourcc tag 0x4752384d/'M8RG' codec_id 00D8
fourcc tag 0x4152384d/'M8RA' codec_id 00D8
fourcc tag 0x3047384d/'M8G0' codec_id 00D8
fourcc tag 0x3059384d/'M8Y0' codec_id 00D8
fourcc tag 0x3259384d/'M8Y2' codec_id 00D8
fourcc tag 0x3459384d/'M8Y4' codec_id 00D8
fourcc tag 0x4159384d/'M8YA' codec_id 00D8
fourcc tag 0x4152304d/'M0RA' codec_id 00D8
fourcc tag 0x4752304d/'M0RG' codec_id 00D8
fourcc tag 0x3047304d/'M0G0' codec_id 00D8
fourcc tag 0x3059304d/'M0Y0' codec_id 00D8
fourcc tag 0x3259304d/'M0Y2' codec_id 00D8
fourcc tag 0x3459304d/'M0Y4' codec_id 00D8
fourcc tag 0x4152324d/'M2RA' codec_id 00D8
fourcc tag 0x4752324d/'M2RG' codec_id 00D8
fourcc tag 0x30434c59/'YLC0' codec_id 00DA
fourcc tag 0x30514853/'SHQ0' codec_id 00DD
fourcc tag 0x31514853/'SHQ1' codec_id 00DD
fourcc tag 0x32514853/'SHQ2' codec_id 00DD
fourcc tag 0x33514853/'SHQ3' codec_id 00DD
fourcc tag 0x34514853/'SHQ4' codec_id 00DD
fourcc tag 0x35514853/'SHQ5' codec_id 00DD
fourcc tag 0x37514853/'SHQ7' codec_id 00DD
fourcc tag 0x39514853/'SHQ9' codec_id 00DD
fourcc tag 0x43564d46/'FMVC' codec_id 00DE
fourcc tag 0x52504353/'SCPR' codec_id 00DF
fourcc tag 0x444f4355/'UCOD' codec_id 00E0
fourcc tag 0x31305641/'AV01' codec_id 00E2
fourcc tag 0x4343534d/'MSCC' codec_id 00E4
fourcc tag 0x43475253/'SRGC' codec_id 00E5
fourcc tag 0x344d4d49/'IMM4' codec_id 00E9
fourcc tag 0x30325442/'BT20' codec_id 00EA
fourcc tag 0x4353574d/'MWSC' codec_id 00EB
fourcc tag 0x564d4357/'WCMV' codec_id 00EC
fourcc tag 0x43534152/'RASC' codec_id 00ED
fourcc tag 0x544d5948/'HYMT' codec_id 00EE
fourcc tag 0x43425241/'ARBC' codec_id 00EF
fourcc tag 0x304d4741/'AGM0' codec_id 00F0
fourcc tag 0x314d4741/'AGM1' codec_id 00F0
fourcc tag 0x324d4741/'AGM2' codec_id 00F0
fourcc tag 0x334d4741/'AGM3' codec_id 00F0
fourcc tag 0x344d4741/'AGM4' codec_id 00F0
fourcc tag 0x354d4741/'AGM5' codec_id 00F0
fourcc tag 0x364d4741/'AGM6' codec_id 00F0
fourcc tag 0x374d4741/'AGM7' codec_id 00F0
fourcc tag 0x5243534c/'LSCR' codec_id 00F1
fourcc tag 0x354d4d49/'IMM5' codec_id 00F3
fourcc tag 0x5644564d/'MVDV' codec_id 00F4
fourcc tag 0x4148564d/'MVHA' codec_id 00F5
fourcc tag 0x3033564d/'MV30' codec_id 00F7
fourcc tag 0x31636c6e/'nlc1' codec_id 00F8
fourcc tag 0x00000001/'????' codec_id 10000
fourcc tag 0x00000001/'????' codec_id 10005
fourcc tag 0x00000001/'????' codec_id 1000C
fourcc tag 0x00000001/'????' codec_id 10008
fourcc tag 0x00000001/'????' codec_id 1001F
fourcc tag 0x00000002/'????' codec_id 11006
fourcc tag 0x00000003/'????' codec_id 10015
fourcc tag 0x00000003/'????' codec_id 10017
fourcc tag 0x00000006/'????' codec_id 10007
fourcc tag 0x00000007/'????' codec_id 10006
fourcc tag 0x0000000a/'????' codec_id 15024
fourcc tag 0x00000010/'????' codec_id 11020
fourcc tag 0x00000011/'????' codec_id 11001
fourcc tag 0x00000011/'????' codec_id 1102C
fourcc tag 0x00000017/'????' codec_id 11020
fourcc tag 0x00000020/' ???' codec_id 1100E
fourcc tag 0x00000022/'"???' codec_id 15015
fourcc tag 0x00000031/'1???' codec_id 1501E
fourcc tag 0x00000032/'2???' codec_id 1501E
fourcc tag 0x00000038/'8???' codec_id 12000
fourcc tag 0x00000042/'B???' codec_id 15034
fourcc tag 0x00000045/'E???' codec_id 1100B
fourcc tag 0x00000014/'????' codec_id 1100B
fourcc tag 0x00000040/'@???' codec_id 1100B
fourcc tag 0x00000050/'P???' codec_id 15000
fourcc tag 0x00000055/'U???' codec_id 15001
fourcc tag 0x00000057/'W???' codec_id 12000
fourcc tag 0x00000058/'X???' codec_id 12001
fourcc tag 0x00000061/'a???' codec_id 11003
fourcc tag 0x00000062/'b???' codec_id 11002
fourcc tag 0x00000064/'d???' codec_id 1100B
fourcc tag 0x00000069/'i???' codec_id 11001
fourcc tag 0x00000075/'u???' codec_id 1503F
fourcc tag 0x00000083/'�???' codec_id 15035
fourcc tag 0x000000ff/'�???' codec_id 15002
fourcc tag 0x00000111/'????' codec_id 15034
fourcc tag 0x00000130/'0???' codec_id 15029
fourcc tag 0x00000135/'5???' codec_id 1505A
fourcc tag 0x00000160/'`???' codec_id 15007
fourcc tag 0x00000161/'a???' codec_id 15008
fourcc tag 0x00000162/'b???' codec_id 15025
fourcc tag 0x00000163/'c???' codec_id 15026
fourcc tag 0x00000165/'e???' codec_id 1504F
fourcc tag 0x00000166/'f???' codec_id 15050
fourcc tag 0x00000200/'????' codec_id 1100C
fourcc tag 0x00000215/'????' codec_id 15006
fourcc tag 0x00000216/'????' codec_id 15006
fourcc tag 0x00000270/'p???' codec_id 1501F
fourcc tag 0x0000028e/'�???' codec_id 1505F
fourcc tag 0x0000028f/'�???' codec_id 1101C
fourcc tag 0x00000401/'????' codec_id 1501B
fourcc tag 0x00000402/'????' codec_id 1503A
fourcc tag 0x00000500/'????' codec_id 15041
fourcc tag 0x00000501/'????' codec_id 15041
fourcc tag 0x00001500/'????' codec_id 1501E
fourcc tag 0x00001501/'????' codec_id 15015
fourcc tag 0x00001600/'????' codec_id 15002
fourcc tag 0x00001602/'????' codec_id 15031
fourcc tag 0x00002000/'? ??' codec_id 15003
fourcc tag 0x00002000/'? ??' codec_id 15028
fourcc tag 0x00002001/'? ??' codec_id 15004
fourcc tag 0x00002048/'H ??' codec_id 15045
fourcc tag 0x00002048/'H ??' codec_id 15046
fourcc tag 0x00006c75/'ul??' codec_id 10006
fourcc tag 0x0000706d/'mp??' codec_id 15002
fourcc tag 0x00004143/'CA??' codec_id 15002
fourcc tag 0x0000594a/'JY??' codec_id 14002
fourcc tag 0x0000729a/'�r??' codec_id 15035
fourcc tag 0x0000a100/'?�??' codec_id 15034
fourcc tag 0x0000a106/'?�??' codec_id 15002
fourcc tag 0x0000a109/'?�??' codec_id 15023
fourcc tag 0x0000f1ac/'��??' codec_id 1500C
fourcc tag 0x0000fffe/'��??' codec_id 15060
fourcc tag 0x00005346/'FS??' codec_id 1100D
fourcc tag 0x0000566f/'oV??' codec_id 15005
[ERROR:0@0.019] global cap.cpp:643 open VIDEOIO(CV_IMAGES): raised OpenCV exception:

OpenCV(4.8.1) /io/opencv/modules/videoio/src/cap_images.cpp:253: error: (-5:Bad argument) CAP_IMAGES: can't find starting number (in the name of file): lightning_output.avi in function 'icvExtractPattern'

**Response:**
It seems that there is an error in the code related to the video output file. The program is unable to find the starting number in the file name "lightning_output.avi". 

To fix this issue, you can modify the video output file name in the `detect_lightning` method. Instead of using "lightning_output.avi", you can provide a complete file path with a valid file name. For example, you can use "output/lightning_output.avi" or any other file path that is suitable for your system.

Here's the modified code snippet:

```python
out = cv2.VideoWriter('output/lightning_output.avi', fourcc, frame_rate, (frame_width, frame_height))
```

Make sure to create the "output" directory before running the code.

<details><summary>Metadata</summary>

- Duration: 14345 ms
- Datetime: 2023-10-21T21:14:33.330401
- Model: gpt-3.5-turbo-16k-0613

</details>

**Options:**
```json
{"temperature": 0.5}
```

**Prompt:**
I thought that was declaring the name of a new video to be created?

**Response:**
Apologies for the confusion. Yes, you are correct. The specified file name "lightning_output.avi" is for the new video file that will be created. The error message suggests that there may be an issue with the file's starting number.

To address this, you can try modifying the code to use a different file name for the output video. For example, you can use "output.avi" or any other valid file name.

```python
out = cv2.VideoWriter('output.avi', fourcc, frame_rate, (frame_width, frame_height))
```

Please ensure that you have the necessary write permissions in the current working directory or provide the complete path to the desired output directory.

Let me know if you encounter any further issues.

<details><summary>Metadata</summary>

- Duration: 15187 ms
- Datetime: 2023-10-21T21:17:45.413722
- Model: gpt-3.5-turbo-16k-0613

</details>

**Options:**
```json
{}
```

