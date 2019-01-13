# GRE Vocab Wallpaper

A python script that displays 10 random GRE words each day from a long list of words. The words jumble up each minute so that you can unknowingly perfect 10 complex vocabs every day; without even giving in much effort.

![alt text](https://github.com/asheeshcric/gre-vocab-wallpaper/blob/master/wallpaper.jpg)


## Getting Started

The instructions below will get you a copy of the project up and running on your local machine for development and testing purposes. To get started, clone the repository on a folder that you want.

### Prerequisites

The only thing you will need to run the script is Python3

```
 $ sudo apt-get install python3
```

### Installing

After you get python3 up and running, you need to execute the script on crontab. This ensures that you need not worry about running the script all the time or everytime you open the computer.
For that purpose, open your command line terminal and type in the following command:

```
 $ crontab -e
```

Then paste in the following command at the end of the file:

```
 */1 * * * * cd /path/to/the/repo_folder && /path/to/the/repo_folder/make_wallpaper.py
```
You can google **"How to set up a cronjob"** if the above method doesn't work in windows.

NOTE: You may have to give permission to run the script as a shell command. For that, you can use:

```
 $ chmod u+x make_wallpaper.py
```

Before running the script or letting the cronjob start, you need to set the image "wallpaper.py" as your wallpaper

## Contributions

I would appreciate contributions. Feel free to make a PR and improve this version.


## Built With

* [Python3](https://docs.python.org/3/) - The programming language used


## Authors

* **Ashish Jaiswal** - *Initial work* - [Ashish Jaiswal](http://jashish.com.np)

## Feedback

Feel free to contact for any feedback or information <ashiz2013@gmail.com>

## License

This repository in under the MIT License: [License](https://github.com/asheeshcric/gre-vocab-wallpaper/blob/master/LICENSE)
