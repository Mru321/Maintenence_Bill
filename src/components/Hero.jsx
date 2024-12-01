import React from 'react'
import img from  'd:/New folder (2)/webDev/Project_1/Maintainance_Bill/maintenance_bill_1.0/src/assets/image.png'
import "./Hero.css"

const hero = () => {
  return (
    <div className='hero_container'>
      <div className='div1'>
        {["The Best", "Journey Takes", "You Home"].map((item, index)=>{
          return (
            <h1>{item}</h1>
          );
        })}
      </div>
      <div className='div2'>
        <img id='house' src={img} alt="House" />

      </div>
    </div>
  )
}

export default hero
