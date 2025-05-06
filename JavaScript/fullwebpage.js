function revealMessage(){
    document.getElementById("location_message").style.display = "block"
}
function hideLocation(){
    document.getElementById("location_message").style.display = "none"
}
  
let images = ["https://s1.cdn.autoevolution.com/images/gallery/CHEVROLET-Camaro-SS-3952_67.jpg", "https://cdn.dealeraccelerate.com/verrillo/1/826/98454/1920x1440/2015-chevrolet-camaro-ss", "https://img2.carmax.com/assets/26743624/hero.jpg?width=400&height=300", "https://www.pcarmarket.com/static/media/uploads/galleries/photos/uploads/galleries/12243-vb-auto-chevy-green-camaro/.thumbnails/TRS_8593.jpg/TRS_8593-tiny-2048x0-0.5x0.jpg", "https://www.motortrend.com/uploads/sites/11/2017/06/camaro-zl1-1le-featured-image.jpg"]
    
let counter = 0
  
function change(){
    if (counter <= images.length){
        document.getElementById("main-img").src=images[counter] 
        counter +=1
    }else{
        counter=0
        document.getElementById("img").src=images[counter]
        }
}