import './App.css'
import TeamMember from './components/teamMember'
import Hero from './components/Hero'
import Contact from 'd:/New folder (2)/webDev/Project_1/Maintainance_Bill/maintenance_bill_1.0/src/components/contact' 
import WorkTogether from './components/workTogether'
import Navbar from './components/NavBar'

function App() {
  const name=["Abha", "Varsha", "Swati", "Mrudula"];
  const description=["Data Science", "Web Development"];
  const image=["AbhaPic", "VarshaPic", "SwatiPic", "MrudulaPic"];
  return (
    <div className='container'>
      <Navbar />
      <Hero />
      <div className='heading'>
        <h1>Meet Our Team</h1>
      </div>
      <TeamMember name={name} description={description} />
      <WorkTogether />
      <Contact />
    </div>
  )
}

export default App
