# Setting Up For The API Class

This guide will walk you through the minimal installations required before we begin class.

You do not have to be familiar with any of these tools (and most of you know Git already), simply install them if you don't already have them.

These instructions are specific to the **Microsoft Windows Platform**, but the same tools are necessary and obtainable for other systems as well.

### Anaconda

- Go to [Anaconda's Website](https://www.anaconda.com) on your Windows machine and click the "Download" button.
- When the `.exe` file finishes downloading (it should be a few minutes), open it.
- You can fly through the installation wizard—the defaults are well-chosen and you don't have to check or uncheck any boxes.

### Git

Make sure you have Git installed. If not:

- Go to [Git's Homepage](https://git-scm.com) and press the "Download for Windows" button.
- Press the "Click here to download" link.
- When the `.exe` file finishes downloading (it should be quick), open it.
- As above, you can fly through the installation, sticking with the defaults, except for:
  - It's a good idea to choose your favorite installed text editor or IDE when that option comes up.
  - The default option for line endings is good for cross-platform compatibility, but your team _may_ have a different opinion about line endings. If you don't know, check!
- If the installer asks you to close apps, and you can't find the ones it's talking about, you can `kill` them using their PID. Drop into PowerShell and run `kill [PID]`for each one, substituting the PID the installer gives you for the `[PID]` part of the command.

### Pick A Text Editor With Good Python Tooling

If you have a text editor you really like already (and who doesn't?), try opening a `.py` file with it, write some quick Python code (any code will do), and as long as you have colored text you'll be absolutely fine using it.

If your favorite editor is too focused on a non-Python language to handle a Python file, and you're looking for something to get up and running quickly with Python, VS Code is a fantastic generalist of a text editor and will prompt you to install Python extensions. Many other generalist text editors will do just fine here as well—Atom, Sublime Text, Emacs, Vim, etc. I'll be using Emacs and am happy to take questions on this odd choice—outside of class time.

If you want a dedicated and powerful Python editor, I've heard great things about PyCharm.

### And You're Done

If you have all that installed, you're ready to begin learning about APIs. See you on Monday!
