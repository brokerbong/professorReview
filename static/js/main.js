function filterList(input, containerId) {
    const value = input.value.toLowerCase();
    const items = document.getElementById(containerId).getElementsByClassName("card");
    for (let i = 0; i < items.length; i++) {
        //console.log(items[i]);
        const text = items[i].innerText.toLowerCase();
        items[i].style.display = text.includes(value) ? "" : "none";
    }
  }
  
  function switchToLectureSearch(keyword) {
    sessionStorage.setItem("lecture_search_keyword", keyword);
    window.location.href = "/?view=lecture";
  }

  function clickProfilePanel(key, id){
    console.log("key: "+key,", id: ", id)

    // 데이터 fetch 및 렌더링
    fetch(`/api/${key}/${id}`)
    .then(res => res.text())
    .then(data => {
      //console.log(data);
      document.getElementById("message-pane").innerHTML = data;
    });

    document.querySelectorAll('.profile-card').forEach(el => el.classList.remove('active'));
    const selected = document.querySelector(`.profile-card[data-id="${id}"][data-type="${key}"]`);
    if (selected) selected.classList.add('active');
  }
  
  
  // document.addEventListener("DOMContentLoaded", function () {
  //   const input = document.getElementById("lectureSearchInput") || document.getElementById("searchInput");
  //   if (input && sessionStorage.getItem("lecture_search_keyword")) {
  //     input.value = sessionStorage.getItem("lecture_search_keyword");
  //     filterList(input, "inbox-list");
  //     sessionStorage.removeItem("lecture_search_keyword");
  //   }
  // });
  