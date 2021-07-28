console.log("hello world");

(() =>
{
    const delete_boxs = document.querySelectorAll(".delete-box img");

    delete_boxs.forEach((delete_box) =>{
        delete_box.addEventListener("click",() =>
        {
            let content = delete_box.getAttribute('data-content');
           let content_id  = delete_box.getAttribute('data-value');
           console.log(content,content_id);
           let p = `  <p>${content}</p>
                    <div class="del-btn-bolck">
                   <button class="delete-content-btn"><a href="/delete_todo/${content_id}">Delete</a></button>
                   <button class="cancel-btn">Cancel</button>
                   </div>` ;
            const section = document.querySelector('.delete-section');
            section.classList.add("active");
            section.innerHTML = p ;
            const cancel_btn = document.querySelector('.cancel-btn');
            cancel_btn.addEventListener("click",()=>
            {
                section.classList.remove("active");
                section.innerHTML = "";
            })
        })
    })
    

})();

(() =>
{
    const toggle_btn = document.querySelector('.toggle_btn');
    toggle_btn.addEventListener("click",() =>
    {
        document.querySelector(".left-section").style.width = 300 +'px' ;
    })
    const close_toggle =document.querySelector(".close_toggle_btn") ;
    close_toggle.addEventListener("click",() =>
    {
        document.querySelector(".left-section").style.width = 0 +'px' ;
    });

})();