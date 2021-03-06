# π¦ Yoda β

**Yoda**
A CLI that takes away the hassle of managing your submission files on different online-judges by
automating the entire process of collecting and organizing your code submissions in one single Directory on your Machine also it distils User Submissions into beautiful Submission HeatMap.

## Highlights
* Downloads your AC solutions from CodeForces,CodeChef and Atcoder and creates a Directory within your Home Directory with the following File Structure:
Contests  
   ```bash
   βββ Contests 
          ββCodeforces  
              βββ<Handle-Name>  
                      βββ<Contest-ID>  
                              βββ <problem-index>  
              βββ<tourist>  
                      βββ 592  
                          βββ A.cpp  
          βββCodeChef   
              βββ<Handle-Name>  
                      βββ <Contest-Name>  
                              βββ <problem-name>  
                                  βββ<problem>  
              βββ<tourist>  
                      βββ AUG20B  
                          βββCHEFWED  
                                  βββCHEFWED.cpp   
          βββAtCoder  
              βββ<Handle-Name>  
                      βββ <Contest-Name>  
                              βββ <problem-level>  
              βββ<tourist>  
                      βββ AtCoder Beginner Contest 230  
                          βββ A.cpp  
   ```     
   
* Supports both Linux and Windows , see [Releases](https://github.com/NikharManchanda/Yoda/releases). 
* Fully automated collection of all yours submissions with minimal effort setup
* Simple and easy and pleasing interface to use interface to get you started in minutes
* Extensive traceability for your submissions for Each OJ , Contest Name , Problem Name with the problem file stored with proper language extension.
* Provides Clear and Beautiful Submission Heatmap of your Accepted Solutions for each Online Judge
 for all three OJ's (FunFact: Atcoder and Codechef doesn't provide you the Submission Heatmap themselves but Yoda does it all π).

## Platforms

Harwest currently has extensive support for the following platforms:
* [Codeforces](https://codeforces.com/)
* [AtCoder](https://atcoder.jp/)
* [CodeChef](https://www.codechef.com/)

While integration with various other OJs are still in the kitchen , your Contributions are always welcomed π.


## Installation

1.) You will require `Python 3.5+` along with `pip3` in order to be able to install and use Yoda.
Refer to the documentation for installing `pip` on [windows](https://phoenixnap.com/kb/install-pip-windows), 
[ubuntu/linux](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)

2.) Install this Github Repository and then enter into that directory in the terminal/command prompt then paste the follwing command:
```bash
$ pip install -e .
```

## Getting Started

After installing the package, run the following command in the terminal:
```bash
$ yoda
```
You'd be greeted with something like this:
```bash
nm@pop-os:~$ yoda

...:βββββββββββββββββββββββββββββββββ:...
...:βββββββββββββββββββββββββββββββββ:...
...:βββββββββββββββββββββββββββββββββ:...
...:βββββββββββββββββββββββββββββββββ:...
...:βββββββββββββββββββββββββββββββββ:...
...:βββββββββββββββββββββββββββββββββ:...
    
   Hey there! π Looks like you're using Yoda for the first time. Let's get you started π
   There are three differnet OJ's from which you can get your User Statistics:
   Atcoder
   CodeForces
   CodeChef

   For each one of the OJ's you can Download all your AC solutions β as well as get your Submission Heatmap!! 
    
   π₯³ You rock! We're good to go now π₯³
```
![yoda](https://www.linkpicture.com/q/LPic61bcf630b9c751790534198.png)   
To use it for a particular OJ run
```bash 
# yoda <platform> 
$ yoda codeforces 
```
```bash
$ yoda atcoder 
```
```bash
$ yoda codechef 
```
![yoda cmd](https://www.linkpicture.com/q/LPic61bcf6839123d1303457515.png)     
Now comes the main part :  
1.)To harvest your submissions from the Codeforces platform.  
Type the following command:  
```bash
# yoda <platform> <command>
$ yoda codeforces download  # example
```
  
You'll be prompted for providing your Codeforces handle name   
```bash
> Enter your prestigious Codeforces Handle : sus #example
```

![Codeforces Download](https://www.linkpicture.com/q/yoda_cfd.jpg)    
![Atcoder Download](https://cdn.discordapp.com/attachments/918887646594474036/921501364247461918/yoda_adf.jpg)    
![CodeChef Download](https://cdn.discordapp.com/attachments/918887646594474036/921501362607497226/yoda_ccd.png)   
Yoda will then start scraping all your AC submissions, starting from most recent submission till your very first submission.  

2.) Get your Submisssion HeatMap:  

Type the following command:  

```bash
# yoda <platform> <command>
$ yoda codeforces graph  # example
```

You'll be prompted for providing your Codeforces handle name  

```bash
> Enter your prestigious Codeforces Handle : vineet4571 #example
```

![CodeChef Heatmap](https://cdn.discordapp.com/attachments/918887646594474036/921501362829803560/yoda_ccg.jpg)  
![Codeforces Heatmap](https://www.linkpicture.com/q/yoda_cfg.png)  
![Atcoder Heatmap](https://cdn.discordapp.com/attachments/918887646594474036/921501362372640818/yoda_ag.png)   
Yoda will then output on a new window your Submission HeatMap !!.  

## Final Directory Look
The Directory then is created after downloading your solution for each OJ and is divided by different handles which is further divided to Contest Dir. then your  Problem Solution finally.     
![File Structure](https://www.linkpicture.com/q/photo_2021-12-18_02-11-07.jpg)   
![File Structure](https://www.linkpicture.com/q/LPic61bcf584b3371734315218.png)   
## License

[MIT License](https://github.com/NikharManchanda/Yoda/blob/main/LICENSE)
