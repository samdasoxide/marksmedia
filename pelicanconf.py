#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'Sammy Ramdas'
SITENAME = "Marks Media"
SITESUBTITLE = 'This will be the tag line'
SITEURL = ''

YEAR = datetime.datetime.today().year

THEME = 'theme'
THEME_STATIC_DIR = 'static'
PATH = 'content'
STATIC_PATHS = ['images', 'mail', 'js', 'css', 'fonts']
EXTRA_PATH_METADATA = {
    'static/images/portfolio': {'path': 'images/portfolio'},
}

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = 'en'
BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'main.css'
FONTS = 'fonts'
SCRIPTS = [
    'jquery-1.11.0.js',
    'bootstrap.min.js',
    'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
    'classie.js',
    'cbpAnimatedHeader.js',
    'jqBootstrapValidation.js',
    'contact_me.js',
    'freeagent.js'
]

DIRECT_TEMPLATES = ['index']

# Top Menu Links
NAVLINKS = (
    ('#page-top', ''),
    ('#services', 'Services'),
    ('#portfolio', 'Portfolio'),
    ('#about', 'About'),
    ('#contact', 'Contact')
)

# Portfolio Name
PORTFOLIO = 'Portfolio'

#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
    ['Name', 'text', 'name', 'Please enter your name.'],
    ['Email Address', 'email', 'email', 'Please enter your email address.'],
    ['Phone Number', 'tel', 'phone', 'Please enter your phone number.'],
    ['Message', 'textarea', 'message', 'Please enter a message.']
)

ADDRESS1 = 'The Internet'
ADDRESS2 = 'Any City, Any Place'
# Left column
ABOUT_LEFT = '''
    <p>At Marks Media production studio we create digital magic.
    Whether you need Studio Quality 3D Animation, 2D Animation, Live Video, Motion Graphics
    or some combination of these techniques to motivate, excite, convince, compel or captivate your audience,
    then we at Marks Media Productions  can bring your story to life and magic to your message.</p>
    <p>Based in Nairobi Kenya, our team of creative and talented artists are dedicated to bringing you the most exciting,
    creative and compelling visuals available on the market today. We manage, direct,
    and produce your entire video project from concept to completion.
    Our award-winning team of experienced artists, writers, producers, and directors,
    will work closely with you to produce your content on time and on budget.</p>

'''
# Right column
ABOUT_RIGHT = '''
    <p>Marks Media Production clients include great companies such as
    Diamond Trust Bank, China Roads and Bridges company, Afrinol Kenya, UN-ICTR, IEBC, and many more.
    We have been delivering hundreds of projects to satisfied customers,
    an achievement Marks Media Production Studio remains proud of.</p>
    <p>Our team of 3D Animators, Producers, Illustrators, Sound Technicians, Writers,
    and Marketing and Branding industry experts listen closely to your goals and strategic objectives,
    and then work with you to develop a timeline and budget to meet your communication needs.
    We can create any kind of Animation, Design, illustration, Video Production,
    Special Effects or graphics you can imagine to convey your message.
    Our experts are committed to working by your side through the creative process,
    from conception to completion. Let us elevate your project to the next level.
    If you can imagine it, we can create it.</p>
'''
# Center
ABOUT_CENTER = '<a href="#" target="_blank" class="btn btn-lg btn-outline"><i class="fa fa-youtube"> Go to my YouTube</i> </a>'
