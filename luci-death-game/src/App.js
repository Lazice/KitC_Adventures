import './App.css';
import Button from './Components/Button';
import {mapMachine} from './Machines/mapMachine.ts';
import {useMachine} from '@xstate/react';

function App() {
  const [state, send] = useMachine(mapMachine);
  
  const coin = new Audio('./Media/coin-toss.wav');
  const dice = new Audio('./Media/dice-roll.wav');
  
  const allocateId = (originalId, ans) => {
    originalId === '0' ? String(ans)
    : String(originalId) + String(ans);
  }

  const searchForId = (id) => {
    for (let i = 0; i < chat.length; i++) {
        if (id === chat[i][-1]){
            return i}
        }
    //chat.find(index => index.id === id) ?.quantity || 0
    return 0
  }
  // const quotedLoc=JSON.stringify(state.value);
  // const loc=quotedLoc.replace(/"([^"]+)":/g, '$1:');

  return (
    <div>
      <div className="game-wrapper">
        <h1 class="box-heading">{JSON.stringify(state.value)}</h1>
        <div className="text-wrapper">
          <p>dialogueeee</p>
        </div>
      </div>
      <Button/>
    </div>
  );
}

export default App;
