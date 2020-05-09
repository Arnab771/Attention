# Attention

## Table of Contents

- [Installation](#Installation)
- [Usage](#Usage)

## Installation

To install you will need Python 3 installed on your system. You may download it from [here.](https://www.python.org)

You can use a virtual environment which is recommended. If you use Pipenv then:

```
git clone https://github.com/Arnab771/Attention.git
cd Attention
pipenv shell
pipenv install
```

Else, you can:

```
git clone https://github.com/Arnab771/Attention.git
cd Attention
pip install -r requirements.txt
```

If you're using Linux or MacOS, you may have to replace the last command with `python3 -m pip install -r requirements.txt`.

## Usage

You can use this script in two ways. Both ways require you to export chat from WhatsApp. If you do not know how to export a chat please search online.

### First Way

If you want to see a graph drawn from overall participation in a chat (which means your chat and the person you chatted with will not be taken seperately, i.e., number of messages will be equal to all the messages sent by you and received by you) you can run:

```
python attention.py [path to exported chat]
```

This is will draw a graph using the exported file.

**Note**: Make sure you are using Python 3. If not you may need to replace `python` with `python3`.

### Second Way

This is probably more useful. You'll be able to put out a graph from that takes the messages of both participants seperately and plots them together.

```
python attention.py [path to exported chat] --split [Name of First Person] [Name of Second Person]
```

The names that you'll provide must be the same as in the exported file.
A typical export looks like this:

```
10/11/19, 9:50 AM - John: Hey
10/11/19, 10:31 AM - Ed: What's up?
```

For this you would run `python attention.py 'WhatsApp Chat with John.txt' --split John Ed`
