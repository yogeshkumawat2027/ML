## instaling Anaconda  
  --- free and open source for programming language Python , R

  still we are using vs code for python and now we will use Anaconda and jupyter lab for data science and ml 

  in Anaconda some packages easily available like Numpy Panadas  around 300 packages

 ** for lightweight project use miniconda

 go to --> anaconda.com/dawnload 

 ![anaconda website](image.png)

 ## Conda Prompt 

 ![alt text](image-1.png)

 normally ek tool ka ek hi version use hota hai ek time par but ham ese diffrent projects me diffrent version par kaam karna chahte hai ya koi logical separation chahiye to uske liye ham multiple *** Environments ** ko create kar sakte hai . Conda help to like this-> package and event management
 
![Conda](image-2.png)

write conda in CLI
>conda

wor windows write commands at anaconda prompt99 ![anaconda prompt](image-3.png)

> conda activate   ---> base environment will create
![alt text](image-4.png)

> conda list --> packages in environment

## creating new environment 
> conda create -n primeenv
then
>conda activate primeenv    ![alt text](image-5.png)

environment delete commands 
1. conda env remove -n NAME
2. conda remove -n NAME --all 
but first conda dectivate
>conda deactivate
> conda env remove -n primeenv


now in base environment 
>conda deactivate    -----> now in normal window

 for base env
 >conda activate      ![alt text](image-6.png)



#####  Installing Jupyter Notebook

![alt text](image-7.png)    ![alt text](image-8.png)

> conda install jupyter
>jupyter notebook   ![alt text](image-9.png)
 .ipynb extension for jupyter notebook -- i python notebook

 difference between file and .ipynb is we can run block of codes or parts of code in single notenook  ![alt text](image-10.png)

 ![alt text](image-11.png)

 ![alt text](image-12.png)

 ![ ](image-13.png) we can devide our code in chunks

 ![ if i save ](image-14.png)


 ### Installing Jupyterlab (Advance of notebook)
 >conda install jupyterlab
 >jupyter lab
  
  its needed for different type of files in single entity

  --> we can create new folder and usi folder me terminal open kar sakte hai. and we can open python notebooks


  **** markdown --> text with code in notebook 
    ![alt text](image-15.png)

    we can restart Kernel and clear outputs of all cells  ![alt text](image-16.png)