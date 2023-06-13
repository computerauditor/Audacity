# Audacity

Audacity is a simple Python script for downloading the videos , audio or even playlists from YouTube!!

## Preview

**Downloading Video/Audio/Playlists using the graphical user interface(GUI):**
![GUI](https://github.com/computerauditor/Audacity/assets/117805200/18183d7c-9bf0-4a45-a14b-7b3343f27c87)

**Downloading Youtube Video[Command-Line]:**

![git video](https://user-images.githubusercontent.com/117805200/213721558-4d1f017d-355d-48a3-a2b0-3ed17a4f9711.png)

**Downloading Whole Playlist from Youtube[Command-Line]:**

![git playlists](https://user-images.githubusercontent.com/117805200/213721886-81c71f51-812d-4544-a0bc-7e015aea1bb8.png)

## Installation

1. We need to install a python library first known as pytube using pip

```pip
pip install pytube
```
2. Clone the repo using git clone
```
git clone https://github.com/computerauditor/audacity.git
```
3. Run the main script using:
```
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
OR
[F-Driod:](https://f-droid.org/en/packages/com.termux/)

[+] Use the following commands in termux to set up python envirnment

1. To upgrade termux default packages 
```
pkg update && pkg upgrade
```
2. To set up python in termux
```
pkg install python
```
3. To set up pytube 
```
pip install pytube
```
4. Then clone the git repo using git clone command
```
git clone https://github.com/computerauditor/audacity.git
```
5. Change directory to the script
```
cd audacity-main/
```
6. Run the script and enjoy!!
```
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/computerauditor/Audacity/blob/main/LICENSE.md)
