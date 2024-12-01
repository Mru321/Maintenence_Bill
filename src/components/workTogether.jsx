import React from 'react'
import './workTogether.css'

function workTogether() {
  return (
    <div>
      <div className='form'>
        <h2>Let's Work Together</h2>
        <div className='info'>
        <form>
          <label htmlFor="name">Name:</label>
          <input type="text" />
          <label htmlFor="phno">Phone Number:</label>
          <input type="text" />
        </form>
        </div>
        <div className='feedback'>
          <form>
            <label htmlFor="feedback">FeedBack:</label>
            <input type="text" />
          </form>
        </div>
      </div>
    </div>
  )
}

export default workTogether
