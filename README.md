# youtube-toolbox
Download youtube video by start_timestamp and duration 

* Good for usage with larger youtube videos that are difficult to deal with due to there large size.
* Eases for reduction data file size down to below 25mb for web management

## Dependencies
### youtube-dl command line tools
#### Linux
available via apt-get
```shell
sudo apt-get install youtube-dl
```

#### Mac with Homebrew

* Homebrew Page: https://brew.sh/

```shell
brew install youtube-dl
```

#### Windows
* Page Link: https://rg3.github.io/youtube-dl/
* Download link: https://rg3.github.io/youtube-dl/download.html

### Test Installation
```shell
youtube-dl --version
```
my sample output:
```shell
2018.09.10
```
## Usage
defaults should work

Arguments
```python
'-vf', '--input-video','input video', default='https://www.youtube.com/watch?v=izTaPcZZAXs'
'-o', '--output_path',help='output location', default='./'
'-ss', '--start', ='specify a start timestamp',default='00:00:05'
'-t', '--duration','encoding duration', default='00:00:10'
```         
### Run program
#### Specify arguments:
youtube video url with option -vf
start time of the clip to download
duration of clip to download

```shell
python get_youtube_part.py -vf 'https://www.youtube.com/watch?v=izTaPcZZAXs' -ss '00:00:05' -t 00:00:10
```
