
function App() {
  let res = [];
  let data = (
    <li className="A" key={0}>
      Hello World!
    </li>
  );
  
  for (let i = 0; i < 10; i++) {
    res.push(
      <li className="A" key={i}>
        Hello World! {i + 1}
      </li>
    );
  }
  
  return (
    <ul>
      {res}
    </ul>
  );
}

export default App;