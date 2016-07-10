# evernote-batch-download
## Python/shell script to download all evernote files with the help of geeknote in structured directories.

Works on Ubuntu, should be easy to update another distribution.

Requires:

* [Geeknote](https://github.com/VitaliyRodnenko/geeknote)

To download Evernote-batch-download:

    git clone https://github.com/sxnwlfkk/evernote-batch-download

Then run:

    ./geeknote-script

The script first checks if `python3` and `expect` is available. If not, it attempts to download them (with `apt-get`). Then it will make a directory ~/evernote, and the folder structure of your notebooks in it. The download takes relatively long time.

### Warning: If you don't have paid account, you might exceed your traffic limit with Evernote. Countermeasures not yet implemented.
