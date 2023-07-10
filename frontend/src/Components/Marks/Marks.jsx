import MarksBox from "./MarksBox"
import Button from "../Button"
import MarkAccurcyConfigure from "./MarkAccurcyConfigure"
import classnames from 'classnames';
import { useState } from 'react'
function Marks({clicked,answers,markings}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  // const answersheets = JSON.parse(localStorage.getItem('answers'));
  // const markingschemes = JSON.parse(localStorage.getItem('markingSceme'));
  // console.log(answers)
  // console.log(markings)
  const [showImages, setShowImages] = useState(false);
  const [error, setError] = useState("");
  const [marksConfigure, setmarksConfigure] = useState([
    {
      "minimum" : "0",
      "maximum" : "30",
      "marks" : "5"
    },
    {
      "minimum" : "30",
      "maximum" : "70",
      "marks" : "10"
    },
    {
      "minimum" : "70",
      "maximum" : "100",
      "marks" : "15"
    }
  ]);
  var length;
  var minimum;

  const handleFormChange = (index, childFormData) => {
    // Update the form data for the specific child component
    const updatedFormData = [...marksConfigure];
    updatedFormData[index] = childFormData;
    if(index<marksConfigure.length-1){
      updatedFormData[index+1].minimum = updatedFormData[index].maximum;
    }
    setmarksConfigure(updatedFormData);
  };

  const handleAddChild = () => {
    // Add a new input fields to add ranges
    length=marksConfigure.length;
    minimum=marksConfigure[length-1].maximum;
    setmarksConfigure([...marksConfigure, 
      {
        "minimum" : minimum,
        "maximum" : "",
        "marks" : ""
      }
    ]);
  };

  const handleRemoveChild = (index) => {
    // Remove a range of input fields in the index
    const updatedFormData = [...marksConfigure];
    updatedFormData.splice(index, 1);
    if(index<marksConfigure.length-1){
      updatedFormData[index].minimum = updatedFormData[index-1].maximum;
    }
    setmarksConfigure(updatedFormData);
  };


  const handleIconClick = () => {
    setShowImages((prev) => !prev);
  };

  const handleProceedClick = () => {
    console.log(marksConfigure)
    marksConfigure.map((markConfigure,index) => {
      if(markConfigure.maximum==="" || markConfigure.marks===""){
        setError("Please fill all the fields")
      }else if(markConfigure.marks>100 || markConfigure.marks<0 || markConfigure.maximum>100 || markConfigure.maximum<0 || markConfigure.minimum>100 || markConfigure.minimum<0){
        console.log(markConfigure.marks)
        setError("Please enter valid marks.")
      }else if(markConfigure.maximum<=markConfigure.minimum){
        setError("Please enter valid range.")
      }
      return 0;
    })
  }
  console.log(error)

  const handleOKClick = () => {
    console.log(marksConfigure)
  }


  const data = answers.map((answer, index) => (
      <MarksBox
        key={answer.id}
        markingScheme_URL={markings[index].uploadUrl}
        answersheet_URL={answer.uploadUrl}
        answer={answer}
        marking={markings[index]}
        showImages={showImages}
      />
      // console.log(markings[index])
    ));

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      <p className="text-center text-[#191854] text-xl font-bold">Configure Marks</p>
      <p className="text-center font-medium">Add marks allocated for each range(mark for student's answer obtained accuracy)</p>
      {/* <button onClick={handleIconClick}>View All</button> */}
      <div className="flex flex-col items-center mb-16">
        <div>
          <MarkAccurcyConfigure marksConfigure={marksConfigure} handleAddChild={handleAddChild} handleRemoveChild={handleRemoveChild} handleFormChange={handleFormChange} error={error}/>
        </div>
        <div className="flex flex-row">
          <Button onClick={handleOKClick} classNames="w-24 text-center bg-custom-blue-2 mt-2 mr-2">Ok</Button>
          <Button onClick={handleProceedClick} classNames="w-24 text-center bg-custom-blue-2 mt-2">Proceed</Button>
        </div>
      </div>
      {
        showImages ? <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-2 absolute left-[85%] mt-2">Hide All</Button>
        : <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-2 absolute left-[85%] mt-2">View All</Button>
      }
      {data}
    </div>
  )
}

export default Marks
