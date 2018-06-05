"""
/file template_generator.py

@brief Template page generator.

@author 03difoha

@date 2017

"""
import os
import sys
import re
from shutil import copyfile

HTML_TEMPLATE = '/templates/index.html'
BUILD_TARGET_LOCATION = '/'

def validateTitle(title):
    """
    Validates title parameter
    :param title of the project:
    :return: validated title of the project
    """
    if 0 < len(title) < 21:
        print('title valid')
        return title
    elif title == '':
        print('No title entered - please enter a title')
        return None
    else:
        print(title)
        print('Invalid title - must not contain over 20 characters')
        return None


def validateId(Id):
    """
    Validates ID parameter
    :param Id of the project:
    :return: validated Id of the project
    """
    try:
        Id = int(Id)
    except:
        Id = Id
    if isinstance(Id, int) and 6 < len(str(Id)) < 8:
        print('Id valid')
        return Id
    elif not isinstance(Id, int):
        print(Id)
        print('Invalid ID - numerical characters only')
        return None
    elif len(str(Id)) < 6 or len(str(Id)) > 8:
        print('Invalid ID - must contain between 6 and 8 characters')
        return None


def validateVersion(version):
    """
    Validates version
    :param build version (int):
    :return: validated version
    """
    if not re.match('^[ 0-9a-zA-Z]+$', version):
        print('Invalid version - must not contain special characters.')
        return None
    else:
        print('version valid')
        return version


def paramStringConsructor(urlParams):
    """
    converts a dictionary containing URL params into a string
    note: if there are no URL parameters defined, this will return an empty string.
    :param dict:
    :return: string of formatted URL params, or empty string if no URL params are set to True
    """
    paramList = ['']
    for key, value in urlParams.items():
        if value:
            paramList.append('{}={}'.format(str(key), str(value)))
            paramList.append('&')
    if any(paramList):
        paramList.insert(0, '?')
        del paramList[-1]

    result = ''.join(paramList)
    print(result)
    return(result)


def generate_build(title, Id, version, urlParams):
    """
    Dynamically generates html page.
    :param validated title:
    :param validated Id:
    :param validated version:
    :return: auto-generated index.html
    """
    validateTitle(title)
    validateId(Id)
    validateVersion(version)
    paramString = paramStringConsructor(urlParams)
    if os.path.exists(BUILD_TARGET_LOCATION):
        os.remove(BUILD_TARGET_LOCATION)
    try:
        copyfile(HTML_TEMPLATE, BUILD_TARGET_LOCATION)
        build = open(BUILD_TARGET_LOCATION, "r")
        contents = build.readlines()
        build.close()
        contents.insert(4, '<title>{}</title>'.format(title))
        contents.insert(89, '<p class="main-title">{}</p>'.format(title))
        contents.insert(91, '<p class="sub-title">Version {}</p>'.format(version))
        contents.insert(95, '<iframe src="//example.com/{}/{}"></iframe>'.format(Id, paramString))
        # Magic numbers ^ refer to the line number of the generated html file
        build = open(BUILD_TARGET_LOCATION, "r+")
        contents = "".join(contents)
        build.write(contents)
        build.close()
        return
    except IOError as e:
        print('New build generation failed :(')
        print(e)
        return None



if __name__=='__main__':
    urlParams = {'autoplay': sys.argv[4],
                 'muted': sys.argv[5],
                 'timeStamp': sys.argv[7],
                 'customSkin': sys.argv[9],
                 'loop': sys.argv[10]
                 }

    generate_build(title=sys.argv[1], Id=sys.argv[2], version=sys.argv[3], urlParams=urlParams)

