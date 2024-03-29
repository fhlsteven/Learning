/* jshint esversion:9 */
// window.addEventListener 属于 Firefox 和 Chrome 
// window.addEventListener('DOMContentLoaded', handler, false);   //firefox
// window.addEventListener('load', handler, false); // Chrome
// window.attachEvent('onload',f); IE 需要用这个
window.addEventListener("load", async()=>{   
    console.log("lodaded");
    let getAll = document.getElementById("getAll");
    let saveAsMhtml = document.getElementById("saveMhtml");
    let clearAd = document.getElementById("clearAd");

    getAll.addEventListener("click", async()=>{
        let[tab] = await chrome.tabs.query({active:true, currentWindow:true});
        chrome.scripting.executeScript({
            target:{tabId:tab.id},
            function:findBlogsInfo,
            args:[ARTICLE_LIST_CLASS_NAME]
        });
    });

    saveAsMhtml.addEventListener("click",async()=>{
        let [tab] = await chrome.tabs.query({active:true, currentWindow:true});
        chrome.pageCapture.saveAsMHTML({tabId:tab.id},(mhtmlData)=>{
            saveAs(mhtmlData, tab.title+'.mhtml');
        });
    });

    clearAd.addEventListener("click", async()=>{
        let [tab] = await chrome.tabs.query({active:true, currentWindow: true});
        chrome.scripting.executeScript({
            target:{tabId:tab.id},
            function:clearAds
        });
    });
});

function clearAds() {
    let ads = document.querySelector("#csdn-toolbar>:first-child");
    ads.style.display = "none";
}

function findBlogsInfo(articleListClassName){
    let articlists = document.querySelectorAll(`.${articleListClassName} li`);
    let articles = new Array();

    for(let article of articlists){
        let articleinfo ={};
        articleinfo.href = article.querySelector("a").href;
        articleinfo.name = article.querySelector("h2").innerText.replace("原创","").trim();
        articleinfo.date = article.querySelector(".column_article_data span").innerText;
        articleinfo.index = 0;
        articles.push(articleinfo);
    }
    document.getElementsByTagName("body")[0].innerHTML='';

    for(let i =articles.length-1;i>=37;i--){
        articles[i].index = i;
        getHtmlInfo(articles[i]);
        sleep(1500);
    }  
      
    hideAllDiv();

    function getHtmlInfo(articleDetail){
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function(){
            if(xhr.status ==200 && xhr.readyState ==4){
                let div = document.createElement("div");
                div.id = "articalinfo";
                div.innerHTML = xhr.responseText;
                div.dataset.index= articleDetail.index;
                document.getElementsByTagName("body")[0].appendChild(div);
                sleep(1000);
            }
        };
        xhr.open("get",articleDetail.href,false);
        xhr.send(null);
    }

    function hideAllDiv(){
        let divs = document.getElementsByTagName("div");
        for(let div of divs){
            if(div.id != "articalinfo"){                    
                div.style.display='none';
            }
        }

        let asides = document.getElementsByTagName("aside");
        for(let aside of asides){
            aside.style.display='none';
        }

        let divShows = document.querySelectorAll("main .blog-content-box div");
        for(let div of divShows){
            div.style.display="";
        }

        let mainboxs = document.querySelectorAll("#mainBox");
        for(let div of mainboxs){
            div.style.display='block';
            div.parentElement.style.display='block';
            div.classList.remove("container");
        }

        let mainarticle = document.getElementsByClassName("blog-content-box");
        for(let div of mainarticle){
            div.style.display="block";
        }
    }

    function sleep(millis){
        var date = new Date();
        var curDate = null;
        do { curDate = new Date(); }
        while(curDate-date < millis);
    }
}

function constructBlogs(){
    document.createElement("options");
}

