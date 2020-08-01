# Getting Started With the PRP

# 1.

Sign in with your Caltech credentials at https://nautilus.optiputer.net/ , and as an admin, I can approve you to start using the free computing power offered to researchers. 

Once you have signed in and I have approved you, get your config file by clicking "Get Config" in the upper right hand corner

![Image of get config](https://github.com/resace3/Image-Processing-and-Analysis-on-the-PRP/blob/master/docs/Capture.PNG)

Once you have your config file, you can place should place it in a .kube folder in your home direcotry ( ~/.kube/config ). 
Windows: C:\Users\Nick Rezaee\.kube\config
Mac: /Users/Nick Rezaee/.kube/config

Once you have the config file in the right folder, you can start running scripts on the PRP via Kubernetes.

In order to run your script, you will need to put it in a docker container, which will run inside a Kubernetes pods. 
(Here is some good links on [Docker](https://www.youtube.com/watch?v=YFl2mCHdv24) and [Kubernetes](https://www.youtube.com/watch?v=L1ie8negCjc))

![Kube in Pod](https://github.com/resace3/Image-Processing-and-Analysis-on-the-PRP/blob/master/docs/kube_in_docker.PNG)

# 2.

You will have to first download Docker [here](https://docs.docker.com/get-docker/).

Once you download docker be sure to enable kubernetes by going into the Docker Desktop App:

![Enable Kubernetes](https://github.com/resace3/Image-Processing-and-Analysis-on-the-PRP/blob/master/docs/enable_kubernetes.PNG)

Chekc

# 3. 

Once you have followed the above steps, you should be able to run the hello_world.yaml file with **kubectl apply -f hello_world.yaml**

In order to see what if your pod is running, you can run **kubectl get pods** 

If you want a comprehensive description of the pod, you can run **kubectl describe pod hello-world**

In order to see the logs or outputs of the *hello-world* Kubernetes Pod created, run **kubectl logs hello-world**

# 4. Create Your Customized Docker Container for your pod.

In order to get the right files into your Kubernetes Pod, you must first create your own Docker container. You will have to use a **Dockerfile** to create your own Docker container (Here is a good ![link](https://www.youtube.com/watch?v=j_o-m8l_8Jg) with some information on Dockerfiles.

The Dockerfile in this repo is used to create a custom Docker container with **docker build -t nrezaee/tiff-ingest .**     
Here is a helpful [link](https://www.youtube.com/watch?v=LQjaJINkQXY) on **docker build**.

After you are done building your container, you should use **docker push nrezaee/tiff-ingest** to push your docker container on to [Dockerhub](https://hub.docker.com/). Dockerhub is the "github" of docker containers. [Here](https://hub.docker.com/search?q=nrezaee&type=image) are the containers made under my docker account and a [link](https://www.youtube.com/watch?v=fdQ7MmQNTa0) with some more info on Dockerhub and **docker push**

# 5. Test Your Container Running in Kubernetes Pod





























































