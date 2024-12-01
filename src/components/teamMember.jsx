import React from 'react'
import './teamMember.css'
import MrudulaPic from "../assets/MrudulaPic.jpeg"
import AbhaPic from "../assets/AbhaPic.jpeg"
import VarshaPic from "../assets/VarshaPic.jpeg"
import SwatiPic from "../assets/SwatiPic.jpeg"

const teamMember = (props) => {
  return (
    <div className='container'>
        <div className='team_member'>
            <p>{props.name[0]}</p>
            <img id='member_img' src={AbhaPic} alt={props.name[0]}/>
            <p>{props.description[0]}</p>
        </div>

        <div className='team_member'>
            <p>{props.name[1]}</p>
            <img id='member_img' src={VarshaPic} alt={props.name[1]} />
            <p>{props.description[1]}</p>
        </div>

        <div className='team_member'>
            <p>{props.name[2]}</p>
            <img id='member_img' src={SwatiPic} alt={props.name[2]} />
            <p>{props.description[1]}</p>
        </div>

        <div className='team_member'>
            <p>{props.name[3]}</p>
            <img id='member_img' src={MrudulaPic} alt={props.name[3]} />
            <p>{props.description[1]}</p>
        </div>
      
    </div>
  )
}

export default teamMember
