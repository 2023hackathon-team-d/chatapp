// TODOリスト
//モーダルを表示させる
const addtodoModal = document.getElementById("add-todo-modal");
const deletetodoModal = document.getElementById("delete-todo-modal");

const addtodoPageButtonClose = document.getElementById("add-todopage-close-btn");
const deletetodoPageButtonClose = document.getElementById("delete-todopage-close-btn");

const addtodoBtn = document.getElementById("add-todo-btn");

const addtodoConfirmBtn = document.getElementById(
  "add-todo-confirmation-btn"
);
const deletetodoConfirmBtn = document.getElementById(
  "delete-todo-confirmation-btn"
);

// モーダルを開く
// <button id="add-todo-btn">チャンネル追加</button>ボタンがクリックされた時
addtodoBtn.addEventListener("click", () => {
  todomodalOpen("add");
});

function todomodalOpen(mode) {
  if (mode === "add") {
    addtodoModal.style.display = "block";
  } else if (mode === "delete") {
    deletetodoModal.style.display = "block";
  } else if (mode === "update") {
    updatetodoModal.style.display = "block";
  }
}

// モーダル内のバツ印がクリックされた時
addtodoPageButtonClose.addEventListener("click", () => {
  todomodalClose("add");
},);
deletetodoPageButtonClose.addEventListener("click", () => {
  todomodalClose("delete");
},);

function todomodalClose(mode) {
  if (mode === "add") {
    addtodoModal.style.display = "none";
  } else if (mode === "delete") {
    deletetodoModal.style.display = "none";
  } else if (mode === "update") {
    updatetodoModal.style.display = "none";
  }
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addtodoModal) {
    addtodoModal.style.display = "none";
  } else if (e.target == deletetodoModal) {
    deletetodoModal.style.display = "none";
  }
}

