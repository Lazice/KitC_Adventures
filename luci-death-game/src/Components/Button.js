import React from 'react'
import './Button.css'

function Button() {
  let audio = new Audio('./Media/coin-toss.wav');
  
  const Play = () => {audio.play()}
  
  return (
    <div>
      <button onClick={Play}>Option 1</button>
    </div>
  )
}

export default Button
