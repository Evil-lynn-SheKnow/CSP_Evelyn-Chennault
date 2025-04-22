let images = ["https://media.ed.edmunds-media.com/dodge/challenger/2023/oem/2023_dodge_challenger_coupe_gt_fq_oem_1_1600.jpg", "https://www.supercars.net/blog/wp-content/uploads/2016/03/2009_Chevrolet_CamaroSS2.jpg"]

function hello(){
    document.getElementById("title").innerHTML = "Hello World"
}
function hover(){
    document.getElementById("image").src = "https://media.ed.edmunds-media.com/dodge/challenger/2023/oem/2023_dodge_challenger_coupe_gt_fq_oem_1_1600.jpg"
}
function leave(){
    document.getElementById("image").src ="https://www.supercars.net/blog/wp-content/uploads/2016/03/2009_Chevrolet_CamaroSS2.jpg" 
}