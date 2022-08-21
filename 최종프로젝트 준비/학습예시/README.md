대표로 선정된 분의 작품을 보니. 나와 비슷하게 한것 같다. 하지만 조금 다르다. 특히 편의성 부분에서 상당히 다르다. 나는 작품 조금만 더 들어와도 모양을 다시 맞추어야 하는데. 이분은 그렇지는 않다. 
.box {
  background-color: white;
  display: grid;
  grid-template:
  "name . desc" max-content
  "img img img" 1fr
  "year . a" max-content / max-content 1fr max-content;
}일단, grid를 이용해서 박스 모양을 맞추는것이 인상이 깊었다. 그 다음에 js에서 이름을 넣는 방식을 택했는데. html에서 하나하나 이름 넣는데 상당한 공을 들였던 나로써는 꽤 인상적이었다. 관리하기 훨씬 편해 보였다. 
 그리고 이 기능
    <header>
      <select id="select-year">
        <option value="All">Year: All</option>
        처음 보는 기능인데 상당히 쓸만해 보인다. 다음에 참고해도 괜찮을 것 같다. 
.image {
  position: relative;
  width: 100%;
  height: 0;
  overflow: hidden;
  padding-bottom: 63.9%;
}

.image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
이 기능은 생각하다가 실행이 안될 거 같다 생각한 건데. 이렇게 실행하면 되는구나. 좋은 정보를 알았다. 
그나저나 내가 궁금했던건 보이는 작품 갯수에 따라 전체 높이를 조절하는 기능인데. 안보인다. 아마, 내가 무엇가를 오해 했던건 아닌가 싶은데. 다음에 전체 높이에 대해 다시 테스트 해 봐야 겠다. 