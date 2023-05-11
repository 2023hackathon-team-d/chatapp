const pagination = () => {
  // 初期設定
  let page = 1; // 今何ページ目にいるか
  const STEP = 3; // ステップ数（1ページに表示する項目数）
  // 全ページ数 channelsリストの総数/ステップ数の余りの有無で場合分け
  // 余りがある場合はページを１つ余分に追加する
  const TOTAL =
    channels.length % STEP == 0
      ? channels.length / STEP
      : Math.floor(channels.length / STEP) + 1;

  // <ul class="pagination"></ul> の中身(li)を書き換える
  const paginationUl = document.querySelector(".pagination");
  let pageCount = 0;
  while (pageCount < TOTAL) {
    let li = document.createElement("li");
    li.innerText = pageCount + 1;
    paginationUl.appendChild(li);
    pageCount++;
  }

  // <ul class="channel-box"></ul> の中身(li)を書き換える
  const show = (page, STEP) => {
    const ul = document.querySelector(".channel-box");
    // 一度リストを空にする
    ul.innerHTML = "";

    const first = (page - 1) * STEP + 1;
    const last = page * STEP;
    console.log(uid);
    channels.forEach((item, i) => {
      if (i < first - 1 || i > last - 1) return;
      const a = document.createElement("a");
      const li = document.createElement("li");
      const url = `/detail/${item.id}`;
      a.innerText = item.name;
      a.setAttribute("href", url);
      a.classList.add("list_a");
      li.appendChild(a);

      //// もしチャンネル作成者uidとuidが同じだったら削除ボタンを追加
      if (uid === item.uid) {
        const deleteButton = document.createElement("button");
        const editButton = document.createElement("button");
        deleteButton.classList.add("list_delete_btn");
        editButton.classList.add("list_edit_btn");
        li.appendChild(deleteButton);
        li.appendChild(editButton);
        deleteButton.addEventListener("click", () => {
          modalOpen("delete");
          const confirmationButtonLink = document.getElementById(
            "delete-confirm-link"
          ); // aタグ
          const url = `/delete/${item.id}`;
          confirmationButtonLink.setAttribute("href", url);
        });
        editButton.addEventListener("click", () => {
          modalOpen("update");
          const confirmationButtonLink = document.getElementById(
            "edit-confirm-link"
          ); // aタグ
          const url = `/update/${item.id}`;
          confirmationButtonLink.setAttribute("href", url);
        });
      }
      /////
      ul.appendChild(li);

      const channel_detail = document.createElement("p");
      channel_detail.innerText = item.abstract;
      channel_detail.classList.add("list_channel_detail");
      li.appendChild(channel_detail);
    });
  };
  // pagination内で現在選択されているページの番号に色を付ける
  const colorPaginationNum = () => {
    // <ul class="pagination"></ul>内の<li></li>を全て取得し、配列に入れる
    // ループさせて一度全ての<li></li>から　class="colored"を削除
    const paginationArr = [...document.querySelectorAll(".pagination li")];
    paginationArr.forEach((page) => {
      page.classList.remove("colored");
    });
    // 選択されているページに　class="colored"を追加（背景色が変わる）
    paginationArr[page - 1].classList.add("colored");
  };

  // 最初に1ページ目を表示
  show(page, STEP);

  // 前ページ遷移
  document.getElementById("prev").addEventListener("click", () => {
    if (page <= 1) return;
    page = page - 1;
    show(page, STEP);
    colorPaginationNum();
  });

  // 次ページ遷移
  document.getElementById("next").addEventListener("click", () => {
    if (page >= channels.length / STEP) return;
    page = page + 1;
    show(page, STEP);
    colorPaginationNum();
  });
};

window.onload = () => {
  pagination();
};
