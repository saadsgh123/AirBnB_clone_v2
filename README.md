<h1 align="center">ALX_AIRBNB_V2</h1>
<p align="center">An AirBnB clone.</p>

<p align="center">
  <img src="https://github.com/bdbaraban/AirBnB_clone_v2/blob/master/assets/hbnb_logo.png"
	    alt="HolbertonBnB logo">
</p>
## Description :house:

HolbertonBnB is a complete RESTful web application, integrating file and
database (MySQL) storage in a back-end API with front-end interfacing in a
clone of AirBnB. The front-end is designed using HTML5/CSS3 and is served using
Python Flask. The application is configured on a distributed system - two web
servers and one load balancer - with Nginx and HAProxy.

HolbertonBnB is still in active development, with complete functionality set to
deploy in the coming month:

* Complete integration of a RESTful API
* Full configuration of website with domain name
* Serving of dynamic content using JavaScript

<p align="center">
  <img src="https://github.com/bdbaraban/AirBnB_clone_v2/blob/master/assets/hbnb_stack.png"
	    alt="HolbertonBnB stack">
</p>

---

## NOTE TO 2019 LYFT SOFTWARE ENGINEERING APPRENTICESHIP RECRUITER

This web app has been the capstone project of my full-stack education at
Holberton School and I want to show it off as a demonstration of all the
skills I've learned at this school.

With that said, I must clarify that it is not complete. As mentioned, the
clone is a work-in-progress, with full deployment as a RESTful API still to
come. Finishing touches will be occurring over the next month, my final at
Holberton.

Recognizing that I am sharing a near-complete project, I additionally put
together a small Flask app according to the specifications described in the
application. Please take a look at this separate repository here:

https://github.com/bdbaraban/lyft_apprenticeship_application

Nonetheless, allow me to talk a little more about this AirBnB clone. This
repository is the second iteration of the project. In the first version
(viewable [here](https://github.com/bdbaraban/AirBnB_clone)), I, together
with a cohort mate, built up the initial file storage back-end and
console from scratch. We pair programmed for most all of this version one work.

In this second iteration of the project, I, together with a new partner,
inherited a different version of the same back-end written by a pair of
Holberton students from an older cohort. We then pair programmed
to build up the database storage engine of the back-end.

In between each version, I put together an entire CSS-styled HTML web page
for the project. This front-end development was coded independently, although
the HTML files I personally wrote are only posted in
[version one](https://github.com/bdbaraban/AirBnB_clone) (the
[web_static](./web_static) folder in this directory was included in the
fork). Addtionally, all Shell, Puppet, and Fabric deployment scripts/manifests
were coded myself.

The README's in both repositories were almost exclusively written myself.
I hope this helps clear things up. I apologize for the confusing versioning, but
the takeaway is that I've been directly involved in coding at least _an_ implementation
of everything in this repository. And hey, software development is no fun without
some confusing version control, right? :sweat_smile: :sob:

Please let me know if you have any questions!

---

### Static :page_facing_up:

The front-end of HolbertonBnB was designed from scratch using HTML5/CSS3 pages
integrated using Flask. While the front-end has not yet been officially deployed,
screenshots are viewable in the README of the [web_flask](./web_flask) directory.

### Classes :cl:

HolbertonBnB supports the following classes:

* BaseModel
* User
* State
* City
* Amenity
* Place
* Review
## Storage :baggage_claim:

The above classes are handled by one of either two abstracted storage engines,
depending on the call - [FileStorage](./models/engine/file_storage.py) or
[DBStorage](./models/engine/db_storage.py).

### FileStorage

The default mode.

In `FileStorage` mode, every time the backend is initialized, HolbertonBnB
instantiates an instance of `FileStorage` called `storage`. The `storage`
object is loaded/re-loaded from any class instances stored in the JSON file
`file.json`. As class instances are created, updated, or deleted, the
`storage` object is used to register corresponding changes in the `file.json`.
