import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Subjects from '../Components/Subjects/Subjects'
import Papers from '../Components/Papers'
import {useEffect, useState} from 'react'
import { useParams } from "react-router-dom";
import axios from 'axios'

function PapersPage() {
  const {year , subjectId} = useParams()
  console.log(year,subjectId)
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  if(!allItems){
    window.location.href="/";
  }
  // console.log(allItems);
  const user_id=allItems['user_id'];
  const userType = allItems['user_role'];
  const accessToken = localStorage.getItem('accessToken')
  const [isClicked,setClick] = useState("inner");
  const [subjects,setSubjects] = useState([]);

//   useEffect(()=>{
//     fetchSubjects();
//   },[]);

//   const fetchSubjects = async () =>{
//       const headers = {
//         Authorization: `Bearer ${accessToken}`,
//       };
//       //****Methana subjects code eken group karaganna oona
//       // console.log(headers)
//       if(userType==="admin"){
//         axios
//         .get(`/subjects/${user_id}`, {headers})
//         .then((response) => {
//           const data = response.data;
//           setSubjects(data);
//         })
//         .catch((error) => {
//           console.error(error);
//         });
//       }else if(userType==="teacher"){
//         // console.log(headers);
//         axios
//         .get(`/subjects/${user_id}`, {headers})
//         .then((response) => {
//           const data = response.data;
//           setSubjects(data);
//         })
//         .catch((error) => {
//           console.error(error);
//         });
//       }
    
//   }
  // console.log("Subjects:",subjects)
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
      <NavBar black onClickFunc={handleClick} clicked={isClicked}/>
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      <Papers clicked={isClicked} data={subjects}/>
    </div>
  )
}

export default PapersPage
