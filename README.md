# Audacity

Audacity is a simple Python script for downloading the videos , audio or even playlists from YouTube!!


## Installation

We need to install a python library first known as pytube using pip

```pip
pip install pytube
```
Clone the repo and 

```python

# Clone the repo using git clone:
https://github.com/computerauditor/audacity.git

# Run the main script using:
python main.py

```
## Usage

```
# General Command

[+] Type "1" for downloading Video
[+] Type "2" for downloading Audio
[+] Type "3" for downloading Playlists

# Paste the URL from YouTube and Let the script do its magic!!

```

## Installing Audacity on Android

Since this script is based on python it is cross platform, here are a few simple steps about how to install this on an android device:

[+] Download a python client my favorite is termux(which is also open source) you can find it over here:
[Google Play Store:](https://play.google.com/store/apps/details?id=com.termux&hl=en_IN&gl=US)
#OR
[F-Driod:](https://f-droid.org/en/packages/com.termux/)

[+] Use the following commands in termux to set up python envirnment

To upgrade termux default packages 
```
pkg update && pkg upgrade
```
To set up python in termux
```
pkg install python
```
To set up pytube 
```
pip install pytube
```

Then clone the git repo using git clone command
```
https://github.com/computerauditor/audacity.git
```
Change directory to the script
```
cd audacity-main/
```
Run the script and enjoy!!
```
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](url)
