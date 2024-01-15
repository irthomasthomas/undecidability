**Prompt:**
Console output during zsh initialization detected.

When using Powerlevel10k with instant prompt, console output during zsh
initialization may indicate issues.

You can:

  - Recommended: Change ~/.zshrc so that it does not perform console I/O
    after the instant prompt preamble. See the link below for details. \n .zshrc \n # Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi
cat $HOME/Reminder-words.text
echo kagi

xmodmap -e "keycode 66 = Shift_L NoSymbol Shift_L"
#echo -e "keymaps 0-127\nkeycode 58 = Shift" | sudo loadkeys -

gov_status=`cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor`

if [ "$gov_status" != "performance" ]; then
  sudo cpupower frequency-set -g performance
fi


source /home/tommy/Development/scripts/shell_functions.sh
source /home/tommy/Development/scripts/llm_shell_functions.sh

OPENAI_API_KEY=$(cat /home/tommy/Development/ai/openai/openai_key)
export OPENAI_API_KEY

export EDITOR="fleet"

# Use powerline

USE_POWERLINE="true"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi
## Add kdesrc-build to PATH

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above thihighlights block; everything else may go below.
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.

setopt EXTENDED_HISTORY
HIST_STAMPS="yyyy-mm-dd"
HISTSIZE=999999999999
SAVEHIST=$HISTSIZE


plugins=(git)
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

export PATH=/home/thomas/.local/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/tommy/.dotnet/tools:/opt/rocm/bin:/opt/rocm/rocprofiler/bin:/opt/rocm/opencl/bin:/opt/rocm/hip/bin:/opt/rocm/bin:/opt/rocm/rocprofiler/bin:/opt/rocm/opencl/bin:/opt/rocm/hip/bin:/home/tommy/.local/bin:/home/tommy/bin:/home/tommy/.local/share/JetBrains/Toolbox/scripts
export PATH=$PATH:$HOME/.local/bin
export PATH="$HOME/kde/src/kdesrc-build:$PATH"
export PATH="/home/tommy/jetbrains:$PATH" 
export PATH="/usr/bin/vendor_perl:$PATH"
export PATH=$PATH:$HOME/.cargo/bin

#
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

PATH="$HOME/perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="$HOME/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="$HOME/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"$HOME/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=$HOME/perl5"; export PERL_MM_OPT;

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

autoload -U +X compinit && compinit
autoload -U +X bashcompinit && bashcompinit

# kdesrc-build #################################################################

alias readability="shot-scraper javascript -i $HOME/Development/scripts/readability.js"

## Autocomplete for kdesrc-run
function _comp_kdesrc_run
{
  local cur
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"

  # Complete only the first argument
  if [[ $COMP_CWORD != 1 ]]; then
    return 0
  fi

  # Retrieve build modules through kdesrc-run
  # If the exit status indicates failure, set the wordlist empty to avoid
  # unrelated messages.
  local modules
  if ! modules=$(kdesrc-run --list-installed);
  then
      modules=""
  fi

  # Return completions that match the current word
  COMPREPLY=( $(compgen -W "${modules}" -- "$cur") )

  return 0
}

## Register autocomplete function
complete -o nospace -F _comp_kdesrc_run kdesrc-run
export PATH=$PATH:/home/thomas/.local/share/JetBrains/Toolbox/scripts

# If not running interactively, don't do anything
# [[ $- != *i* ]] && kdialog --msgbox "REMEMBER TO INSTALL LIVECAPTIONS"
# echo "remember to install LiveCaptions"
# kdialog --title "Important Reminder" --msgbox "Open dolphin and browse to Tags:// \n Use simonw symbex llm and strip-tags"
alias issues='gh issue list'
export funcs=$HOME/Development/scripts/shell_functions.sh
export llmfuncs=$HOME/Development/scripts/llm_shell_functions.sh


# [[ -z "$RECORDING_ON" ]] || source /home/tommy/Development/scripts/session-recorder.sh

**Response:**
The console output during zsh initialization indicates that there may be issues with the initialization process. Some potential issues are:

1. Console I/O after the instant prompt preamble: If there are any code blocks in your .zshrc file that require console input (password prompts, confirmations, etc.), they should be placed above the block that enables Powerlevel10k instant prompt. The console I/O code block should stay close to the top of the .zshrc file, while everything else can go below it.

2. Use of deprecated or invalid commands: The console output shows several commands that may no longer be necessary or may not work as intended. For example:

- The command "cat $HOME/Reminder-words.text" may not be required and could be causing issues.
- The command "xmodmap -e "keycode 66 = Shift_L NoSymbol Shift_L"" could be deprecated or may not work as expected.
- The command "sudo cpupower frequency-set -g performance" may require sudo privileges and could be causing issues.

It is recommended to review and update your .zshrc file to address the potential issues mentioned above.

<details><summary>Metadata</summary>

- Duration: 6669 ms
- Datetime: 2023-08-22T16:52:13.192942
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

