const STEP = 3;
let page = 1; 

const todo_show = (STEP) => {
    const ul = document.querySelector(".everytodo-contana");
    // 一度リストを空にする
    ul.innerHTML = "";

    const first = (page - 1) * STEP + 1;
    const last = page * STEP;
    console.log(uid);
    channels.forEach((item, i) => {
      if (i < first - 1 || i > last - 1) return;
      const p1 = document.createElement("p");
      const p2 = document.createElement("p");
      const li = document.createElement("li");
      p1.innerText = item.todo_status;
      p2.innerText = item.todo_name;
      p1.classList.add("list_todo");
      p2.classList.add("list-bloom");
      li.appendChild(p1);
      li.appendChild(p2);

    });
  };