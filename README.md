# Getting Started With the PRP

The Pacific Research Platfrom (PRP) is a free tool funded by the National Research Foundation for researchers to use. The platform is currently being used by 100+ labs in California. 

Here are links with more infromation on the PRP:

https://pacificresearchplatform.org/

https://citris-uc.org/connected-communities/project/pacific-research-platform-uc-san-diego-uc-berkeley-lead-creation-of-west-coast-big-data-freeway-system/

https://pacificwave.net/files/projects/PRP_Overview_%C6%923.pdf



# 1. Connecting to the Pacific Research Platform

Sign in with your Caltech credentials at https://nautilus.optiputer.net/ , and as an admin, I can approve you to start using the free computing power offered to researchers. 

Once you have signed in, email me and I will approve you.Then you will be able to get your config file by clicking "Get Config" in the upper right hand corner

![Image of get config](https://github.com/resace3/Image-Processing-and-Analysis-on-the-PRP/blob/master/docs/Capture.PNG)

Once you have your config file, you can place should place it in a .kube folder in your home direcotry ( ~/.kube/config ). 
Windows: C:\Users\Nick Rezaee\.kube\config
Mac: /Users/Nick Rezaee/.kube/config

Once you have the config file in the right folder, you can start running scripts on the PRP via Kubernetes.

In order to run your script, you will need to put it in a docker container, which will run inside a Kubernetes pods. 
(Here is some good links on [Docker](https://www.youtube.com/watch?v=YFl2mCHdv24) and [Kubernetes](https://www.youtube.com/watch?v=L1ie8negCjc))

![Kube in Pod](https://github.com/resace3/Image-Processing-and-Analysis-on-the-PRP/blob/master/docs/kube_in_docker.PNG)

# 2. Enabling Docker and Kubernetes

You will have to first download Docker [here](https://docs.docker.com/get-docker/).

Once you download docker be sure to enable kubernetes by going into the Docker Desktop App:

![Enable Kubernetes](https://github.com/resace3/Image-Processing-and-Analysis-on-the-PRP/blob/master/docs/enable_kubernetes.PNG)

Chekc

# 3. Kuberentes Test and Commands

**Before running anything I highly recommend you read https://pacificresearchplatform.org/userdocs/running/jobs/. In the link, they show how to run [Kuberenetes Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) on the PRP, which is similar to running [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/).**

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

Now that have you built your own docker container, you can run and test it in a pod. 

We will build a pod to test the container we built in step 4 with *image_processing/tiff_ingest_test.yaml*. Notice how the **args** section of *image_processing/tiff_ingest_test.yaml* is set to **sleep 1h**. 

We can use **kubectl apply -f tiff_ingest_test.yaml** to start the pod and then use **kubectl exec -it tiff-ingest /bin/bash** to get to the command line of the Kubernetes pod. From here you can start testing scripts that you copied in your Dockerfile. Here is a helpful [link](https://www.youtube.com/watch?v=6q5FfhZRzVQ) on **kubectl exec** 

# 6. Finalizing Your Pod

Once you are sure that your pod is running correctly, you can have your commands automatically run, which is seen in **args** section of *image_processing/tiff_ingest.yaml*.

You can check how your pod is managing resources at https://grafana.nautilus.optiputer.net/d/85a562078cdf77779eaa1add43ccec1e/kubernetes-compute-resources-namespace-pods?orgId=1&refresh=10s&var-datasource=default&var-cluster=&var-namespace=cai-lab 






























































