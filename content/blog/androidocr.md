Title: Java and OCR Text Reading with Android Vision API
Date: 2018-3-31 17:50
Tags: android, mobile, apps, ocr, docker
Slug: androidvision
Category: mobile
Author: Alex Nguyen
Summary: Tinkering with Java/Android -- one surefire way to consume an Easter weekend!


## SpringBoot
Last weekend I spent a lot of time re-familiarising with Java - I've spent a lot of time in the Python space recently. 

I learned how to use [SpringBoot](https://projects.spring.io/spring-boot/) for a take-home which required exposing an API on a Server connected to a MySQL backend and essentially writing a client to pretty print query results.

The general approach was similar to `Flask` in that there are provided annotations that route REST endpoints - you just need to route requests to the right functions and bob's your uncle. The package 

JSON structure/type conversion was somewhat magical -- where with `requests` you parse data structures from strings/ints on raw JSON, using Springboot with `Jackson` in Java provides somewhat implicit conversion. Instead, you make a class that represents your JSON object (though I thankfully didn't need it, nesting works by having wrapper classes made too) and the library handles parsing to the input Object types you require. In my case, I needed dates called as a String to be parsed into a Date - it handled with no fuss which was convenient.

Still, I find myself preferring the ability to interact with objects in Python and the ability to simply `pip install` & `import` stuff instead of fiddling with `maven` XML dependencies and plugins. I would say 50% of project time was dedicated to figuring out how to make my project `.jar` files run from commandline the way they do within the `IntelliJ` IDE!
That could be my fault for not knowing how to configure the IDE to output the right thing for me yet, but it was pretty frustrating.

## Android
This Easter weekend I decided to scratch an itch that has been in my brain for some time - is there a library that provides streamed, locally processed text scanning for mobile app development? Essentially I wanted something in the vein of of a QR Code scanner library, without the need to take pictures to interact with the captured code. Also instead of a QR code, I wanted to manipulate arbitrary text (i.e. optical character recognition) I wanted it to work locally for performance reasons as well as offline functionality. 

Knowing nothing about computer vision, I wanted to find a library to help out with this - rough searching brought up the [Google Vision APIs sample](https://codelabs.developers.google.com/codelabs/mobile-vision-ocr/). I spent the better part of a day (the tutorial takes 30min but I spent time investigating the API) to find it seems to deliver what I was looking for (particularly the local processing part).

I followed the introduction and slightly adapted the result to do further simple text parsing - at a glance it recognises printed text pretty well. I'm hoping to get the time to continue tinkering in the next couple months - I'm envisioning a conversion app I can use by hovering on the fly instead of repeatedly typing numbers into my phone's calculator. For anyone interested, the project currently lives [here](https://github.com/AlexN34/ocrconverter).

## Docker 
My docker (compose) file repo [here](https://github.com/AlexN34/dockerfiles) has now amassed files for running JetBrains IDEs: IntelliJ IDEA, PyCharm and AndroidStudio (this counts, it's based on IntelliJ)! 

Each file took a lot longer than expected to set up because while they all use the same general structure for config storage, they're not *exactly* the same. I kept getting tripped up by the fact that the path looks like `~/{IDE Name}{version}/`; it changes with every resolution. I could probably make it general with symlinking something like `ln -s ~/.{IDE Name} {IDE Name}{version}`in the Dockerfile that builds the image in the first place and forever keeping a singular named repo for `.{IDE Name}`, but for now the files just code in the latest version number. 

One cool thing was that it's possible to get USB passthrough to the docker container (for debugging on device) simply by mounting the `/dev/usb` folder (*everything* is a file) in Linux. Won't work on Windows though as apparently usb passthrough [isn't yet supported](https://forums.docker.com/t/docker-for-windows-usb-support/38693/2) which dampens the dream of crossplatform for now.
