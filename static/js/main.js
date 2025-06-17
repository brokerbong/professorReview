function filterList(input, containerId) {
    const value = input.value.toLowerCase();
    const items = document.getElementById(containerId).getElementsByClassName("card");
    for (let i = 0; i < items.length; i++) {
        //console.log(items[i]);
        const text = items[i].innerText.toLowerCase();
        items[i].style.display = text.includes(value) ? "" : "none";
    }
  }

  function clickProfilePanel(key, id){
    console.log("key: "+key,", id: ", id)

    document.querySelectorAll('.profile-card').forEach(el => el.classList.remove('active'));
    const selected = document.querySelector(`.profile-card[data-id="${id}"][data-type="${key}"]`);
    if (selected) selected.classList.add('active');

    // 데이터 fetch 및 렌더링
    fetch(`/api/${key}/${id}`)
    .then(res => res.text())
    .then(data => {
      //console.log(data);
      document.getElementById("message-pane").innerHTML = data;
    });
  }

  function submitReview(type, id) {
    const container = document.getElementById("message-pane");
    const inputs = container.querySelectorAll("input, textarea, select");
  
    const data = {};
    inputs.forEach(input => {
      if (input.name) data[input.name] = input.value;
    });
  
    fetch(`/api/review/${type}/${id}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(res => {
        if (!res.ok) throw new Error("등록 실패");
        return res.text();
      })
      .then(html => {
        document.getElementById("message-pane").innerHTML = html;
      })
      .catch(err => {
        alert("리뷰 등록에 실패했습니다.");
        console.error(err);
      });
  }
  
  
  // document.addEventListener("DOMContentLoaded", function () {
  //   const input = document.getElementById("lectureSearchInput") || document.getElementById("searchInput");
  //   if (input && sessionStorage.getItem("lecture_search_keyword")) {
  //     input.value = sessionStorage.getItem("lecture_search_keyword");
  //     filterList(input, "inbox-list");
  //     sessionStorage.removeItem("lecture_search_keyword");
  //   }
  // });
  