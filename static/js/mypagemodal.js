const mydreamModal = document.getElementById("mydream-modal");
const mydreamPageButtonClose = document.getElementById("mydream-page-close-btn");
const mydreamConfirmBtn = document.getElementById("mydream-confirmation-btn");
const mydreamBtn = document.getElementById("mydream-btn");


//マイページのモーダルを開く 
mydreamBtn.addEventListener('click', modalOpen);
function modalOpen() {
  mydreamModal.style.display = 'block';
}

// マイページのモーダル内のバツ印がクリックされた時
mydreamPageButtonClose.addEventListener('click', modalClose);
function modalClose() {
  mydreamModal.style.display = 'none';
  }
  

  // マイページのコンテンツ以外がクリックされた時
addEventListener('click', outsideClose);
function outsideClose(e) {
  if (e.target == mydreamModal) {
    modal.style.display = 'none';
  }
}