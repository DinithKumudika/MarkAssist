import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Subjects from '../Components/Subjects/Subjects'
import {useEffect, useState} from 'react'
import axios from 'axios'
function SubjectsPage() {
  const allItems=JSON.parse(localStorage.getItem('token'));
  const user_id=allItems['_id'];
  const userType = allItems['userType'];
  const [isClicked,setClick] = useState("outer");
  const [subjects,setSubjects] = useState([]);

  useEffect(()=>{
    fetchSubjects();
  },[]);

  const fetchSubjects = async () =>{
    try{
      const config = {
        headers: {
          Authorization: `Bearer ${allItems['token']}`,
        },
      }
      //****Methana subjects code eken group karaganna oona
      let response = {}
      if(userType==="admin"){
        response = await axios.get(`http://localhost:5000/api/subjects/${user_id}`,config);
      }else if(userType==="teacher"){
        response = await axios.get(`http://localhost:5000/api/subjects/${user_id}`,config);
      }
      const data = response.data;
      setSubjects(data);
    }catch(error){
      console.log(error);
    }
  }
  //Function to handle the click of the hamburger menu
  const handleClick = () => {
    if(isClicked==="outer"){
    setClick("inner")
    }else{
    setClick("outer")
    }
    // console.log(isClicked)
  }

  return (
    <div>
      <NavBar black onClickFunc={handleClick}/>
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      <Subjects clicked={isClicked} data={subjects}/>
    </div>
  )
}

export default SubjectsPage
