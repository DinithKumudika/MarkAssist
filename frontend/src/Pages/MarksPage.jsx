import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Marks from '../Components/Marks/Marks'
import {useEffect, useState} from 'react'
import { MoonLoader } from 'react-spinners';
import {useParams} from 'react-router-dom'
import axios from 'axios'
function MarksPage() {
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  // console.log(allItems);
  if(!allItems){
    window.location.href="/";
  }
  const user_id=allItems['user_id'];
  const { year,subjectId,paperId} = useParams()
  const [isClicked,setClick] = useState("inner");
  const [marks,setMarks] = useState([]);
  const [answers,setAnswers] = useState([]);
  const [markings,setMarkings] = useState([]);
  const [markingschemeID,setmarkingschemeID] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [isLoading2, setIsLoading2] = useState(true);

  useEffect(()=>{
    // console.log("DATA:");
    fetchData();
  },[]);

  const fetchData = async () =>{
    axios
    .get(`http://127.0.0.1:8000/api_v1/answers/${paperId}`)
    .then((response) => {
      const answer = response.data
      setAnswers(answer)
      setIsLoading(false);
      console.log("Answers:",answer)
      // Process the response data or update your React component state
      axios
      .get(`http://127.0.0.1:8000/api_v1/markings/questions?sub=${subjectId}`)
      .then((response)=>{
        const marking = response.data
        console.log("Markasdfghings:",answers)
        setMarkings(marking)
        // console.log("Markasdfghings:",marking[0].markingScheme)
        setIsLoading2(false);
        setmarkingschemeID(marking[0].markingScheme) 
        axios
        .get(`http://127.0.0.1:8000/api_v1/answers/compare/${marking[0].markingScheme}?sub=${subjectId}&stu=${answer[0].userId}`)
        .then((response)=>{
          const marks = response.data
          // setMarkings(marking)
          // markingschemeID = marking[0].markingScheme
          console.log("Markkkkkkssssss:",marks)

        })
        .catch((error) => {
          console.error(error);
          // setMarks(null)
          // Handle the error, e.g., display an error message to the user
        });
      })
      .catch((error) => {
        console.error(error);
        setMarks(null)
        // Handle the error, e.g., display an error message to the user
      });
    })
    .catch((error) => {
      console.error(error);
      setAnswers(null)
      // Handle the error, e.g., display an error message to the user
    });
    
    // console.log("Markingsss:",answers)
    
  }

  // const fetchData = async () => {
  //   try {
  //     const answerResponse = await axios.get(`http://127.0.0.1:8000/api_v1/answers/${paperId}`);
  //     const answer = answerResponse.data;
  //     setAnswers(answer);
  //     // console.log("Answers:", answer);
  
  //     const markingResponse = await axios.get(`http://127.0.0.1:8000/api_v1/markings/questions?sub=${subjectId}`);
  //     const marking = markingResponse.data;
  //     setMarkings(marking);
  //     // console.log("Markings:", marking);
  
  //     // Both API calls have completed at this point
  
  //     // Proceed with any additional logic or rendering
  //   } catch (error) {
  //     // Handle any errors that occurred during the API calls
  //     console.error(error);
  //   }
  // };


  const handleClick = () => {
    if(isClicked==="outer"){
    setClick("inner")
    // console.log(isClicked)
    }else{
    setClick("outer")
    // console.log(isClicked)
    }
  }
  return (
    <div>
      <NavBar />
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      {/* {markings.length>=answers.length ? <Marks clicked={isClicked} answers={answers} markings={markings}/> : ''} */}
        {(isLoading || isLoading2) ? <MoonLoader color="#36d7b7" height={6} width={128} className='absolute top-[20vw] left-[55%]'/> 
          :<Marks clicked={isClicked} answers={answers} markings={markings}/>
        }

    </div>
  )
}

export default MarksPage
