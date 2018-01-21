#!/usr/bin/env python3
import dominate, configparser, time
from dominate.tags import *
from os import makedirs as mkdir

config = configparser.ConfigParser()
configFile = 'woovienet-config.ini'
print('using %s'%(configFile))
config.read(configFile)
settings = {}

def init():
    #web
    settings['sitename'] = config.get('web', 'sitename')
    settings['url']      = config.get('web', 'url')
    settings['docroot']  = config.get('web', 'docroot')
    buildHome()
    buildAbout()
    buildBlog()
    buildKeyboards()

def buildHome():
    site = {}
    site['html'] = html()
    site['head'] = site['html'].add(head())
    buildHead(site['head'])
    site['head'].add(title('%s | Home'%(settings['sitename'])))
    site['body'] = site['html'].add(body())
    site['body'].add(buildNavbar())
    site['container'] = site['body'].add(div(cls='container'))
    site['container'].add(div(h2('Welcome to my site'), p('Check out links below to my projects', cls='lead'), cls='jumbotron'))
    site['container'].add(div(h3('Current projects'), ul(li(a('mksource.net', href='https://mksource.net'), ', an aggregation of all various keyboard parts on the custom keyboard market. Think of it like Amazon style aggregation, minus the direct selling. It\'s completely free and ad free. You can check out our GitHub organization page ', a('here', href='https://github.com/mksourcenet'), '. The site is written in Python 3.6 using Dominate mostly and some Javascript (JQuery primarily) as well for the front end.'), li(a('coininfo', href='/coin'), ', a vertcoin data analyzer. Written in Python 3.6 and uses uwsgi via nginx proxy.'), li(a('My keyboards', href='/keyboards'), ', I have a few and they are very customized. Dive into the world of a keyboard addict. Shoutouts to ', a('geekhack', href='https://geekhack.org'), ' and ', a('/r/mechanicalkeyboards', href='https://reddit.com/r/mechanicalkeyboards')))))
    output = site['html'].render()
    print('writing to %s/index.html'%(settings['docroot']))
    mkdir(settings['docroot'], exist_ok=True)
    open('%s/index.html'%(settings['docroot']), 'w').write(output)

def buildAbout():
    site = {}
    site['html'] = html()
    site['head'] = site['html'].add(head())
    buildHead(site['head'])
    site['head'].add(title('%s | About'%(settings['sitename'])))
    site['body'] = site['html'].add(body())
    site['body'].add(buildNavbar())
    site['container'] = site['body'].add(div(cls='container'))
    site['container'].add(div(h2('About me'), p('Who I am, what I do.', cls='lead'), cls='jumbotron'))
    site['container'].add(div(p('My name is Jordan Banasik. I live in Houston, TX. I\'m a GED holding Linux nerd who loves to program for fun, but wanting to make a career out of it. Most of what I post on my site is hobby related. My day job is working in Linux environments, mostly RHEL. I got my start with Linux by working for HostGator, who was once easily the best host around. I started in 2014, and was initially held in the first tier position for quite a while. Even after getting to a second tier position, it wasn\'t until I met the Linux trainer that anyone gave me an opportunity to move up. Once I got into the tier 3 training class, I was able to move to an administrator position within a year of that. At HostGator I learned a lot about hosting, Linux, cPanel, security, and general technology regarding the internet. While it wasn\'t a perfect experience, it gave me direction and focus to move up in this industry. I am now working my way to make it into a programming related position. Find me on most social media under the alias Woovie. Feel free to email me as well, woovie at woovie dot net.')))
    output = site['html'].render()
    print('writing to %s/about/index.html'%(settings['docroot']))
    mkdir('%s/about/'%(settings['docroot']), exist_ok=True)
    open('%s/about/index.html'%(settings['docroot']), 'w').write(output)

def buildBlog():
    site = {}
    site['html'] = html()
    site['head'] = site['html'].add(head())
    buildHead(site['head'])
    site['head'].add(title('%s | Blog'%(settings['sitename'])))
    site['body'] = site['html'].add(body())
    site['body'].add(buildNavbar())
    site['container'] = site['body'].add(div(cls='container'))
    site['container'].add(div(h2('My blog'), p('Random thoughts and ideas about projects.', cls='lead'), cls='jumbotron'))
    output = site['html'].render()
    print('writing to %s/blog/index.html'%(settings['docroot']))
    mkdir('%s/blog/'%(settings['docroot']), exist_ok=True)
    open('%s/blog/index.html'%(settings['docroot']), 'w').write(output)

def buildKeyboards():
    site = {}
    site['html'] = html()
    site['head'] = site['html'].add(head())
    buildHead(site['head'])
    site['head'].add(title('%s | Blog'%(settings['sitename'])))
    site['body'] = site['html'].add(body())
    site['body'].add(buildNavbar())
    site['container'] = site['body'].add(div(cls='container'))
    site['container'].add(div(h2('My keyboards'), p('Typing is love, typing is life.', cls='lead'), cls='jumbotron'))
    output = site['html'].render()
    print('writing to %s/keyboards/index.html'%(settings['docroot']))
    mkdir('%s/keyboards/'%(settings['docroot']), exist_ok=True)
    open('%s/keyboards/index.html'%(settings['docroot']), 'w').write(output)

def buildHead(headElement):
    headElement.add(script(src='%s/js/popper.js'%(settings['url'])))
    headElement.add(script(src='%s/js/jquery.min.js'%(settings['url'])))
    headElement.add(script(src='%s/js/bootstrap.min.js'%(settings['url'])))
    headElement.add(link(href='%s/css/bootstrap.min.css'%(settings['url']), rel='stylesheet'))
    headElement.add(link(rel='icon', href='favicon.gif', type='image/gif'))

def buildNavbar():
    navbar = nav(cls='navbar navbar-dark bg-dark navbar-expand-lg')
    navbar.add(a(settings['sitename'], cls='navbar-brand', href=settings['url']))
    navbar.add(button(span(cls='navbar-toggler-icon'), cls='navbar-toggler', type='button', data_toggle='collapse', data_target='#navbarMenu', aria_controls='navbarMenu', aria_expanded='false', aria_label='Open navigation menu'))
    navbar.add(div(ul(li(a('Home', cls='nav-link', href='/'), cls='navbar-item'), li(a('About Me', cls='nav-link', href='/about'), cls='navbar-item'), li(a('Blog', cls='nav-link', href='/blog'), cls='navbar-item'), cls='navbar-nav ml-auto'), cls='collapse navbar-collapse', id='navbarMenu'))
    return navbar

init()
