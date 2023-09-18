import classnames from 'classnames'
import { useState } from 'react'
import { AiFillEye ,AiFillEyeInvisible } from "react-icons/ai";
function MakingSchemeConfigureBox({ index, formData, onChange,showImages}) {
    const [showImage, setShowImages] = useState(false);
    const handleIconClick = () => {
      setShowImages((prev) => !prev);
    };
    // console.log("formdata:",typeof(formData.keywords),formData.keywords.length)
    const keywords = formData.keywords.map((keyword,index) => (
      <input type="text" key={index} value={keyword} className="shadow shadow-gray-500 bg-[#EDEDED] mr-2 h-12 text-center rounded rounded-lg font-bold mb-2" disabled/>
    ))

    var buttonclicked;
    const handleInputChange = (event) => {
        const { name, value } = event.target;
        // console.log(name, value);
        const updatedFormData = {...formData, [name]: value };
        // console.log("formdatas:",updatedFormData);
        onChange(index, updatedFormData);
      };

    const handleSelect = () => {
        console.log("selected");
        const updatedFormData = {...formData, selected: true };
        onChange(index, updatedFormData);
        // buttonclicked = classnames('bg-green-500')
    }

    const handleDeselect = () => {
        console.log("deselected");
        const updatedFormData = {...formData, selected: false };
        onChange(index, updatedFormData);
        // buttonclicked = classnames('bg-red-500')
    }

    const classes = classnames('bg-[#EDEDED] h-10 text-center rounded rounded-lg font-bold w-full ')
    const divclasses = classnames('bg-[#EDEDED] rounded rounded-xl w-full flex flex-row items-center justify-between mb-2 ')
  return (
    <div className="flex flex-col my-6 w-full">
      <p className="font-bold mb-1">{formData.questionNo}  {formData.subQuestionNo} {formData.partNo}</p>
      <div className="w-[100%] bg-[#D4D4D4] rounded-lg flex flex-row max-lg:flex-col">
        <div className="flex flex-row px-2 rounded-lg p-4 w-[80%] bg-[#EDEDED] h-auto max-lg:w-full">
          <div className='w-[95%]'>
              <p className=" p-2 mb-1 mr-1">{formData.text}</p>
             {showImages ? <img  className="w-full h-fit " src={formData.uploadUrl} alt="Marking scheme"/>
                : showImage && <img  className="w-full h-fit " src={formData.uploadUrl} alt="Marking scheme"/>}
            <div className="flex flex-col">
              {/* <p className="text-xl text-[#191854] text-center font-bold my-2">Keywords</p> */}
              {/* <div className="w-full flex justify-between flex-wrap p-2 bg-gray-100"> */}
                {formData?.keywords[0] !== ""  && (<div className="flex flex-col">
                  <p className="text-xl text-[#191854] text-center font-bold my-2">Keywords</p>
                  <div className="grid lg:grid-cols-3 md:grid-cols-2 gap-2 p-2 bg-gray-100">
                    {keywords}
                  </div>
                </div>)}
              {/* </div> */}
            </div>
          </div>
          <div className='basis-[5%]'>
            {showImages ? <AiFillEye onClick={handleIconClick} className='hover:cursor-pointer border-2 border-gray-500 text-4xl z-auto'/> 
              : showImage ?<AiFillEye onClick={handleIconClick} className='hover:cursor-pointer border-2 border-gray-500 text-4xl z-auto'/> 
                  : <AiFillEyeInvisible className='hover:cursor-pointer text-4xl border-2 border-gray-500 z-auto' onClick={handleIconClick}/>}
          </div>
        </div>
        <div className="py-4 flex flex-col justify-between w-[20%] items-center px-2 max-lg:flex-col max-lg:items-center max-lg:w-full">
          <div  className="w-full flex flex-row items-center justify-between mb-2 max-lg:justify-between">
            <button onClick={handleSelect} className={` ${formData.selected===false ? "bg-[#EDEDED]" : "bg-green-500 text-white"} font-bold text-[#191854] bg-[#EDEDED] px-2 rounded rounded-lg w-[45%] h-10 `}>Select</button>
            <button onClick={handleDeselect} className={`${formData.selected===false ? "bg-red-500 text-white" : "bg-[#EDEDED]"} font-bold text-[#191854] bg-[#EDEDED] px-2 rounded rounded-lg w-[45%] h-10 `}>Deselect</button>
          </div>
          <div  className={divclasses}>
            {/* <label className="mr-2">Question no:</label> */}
            <input type="text" name='questionNo' pattern="[0-9]{2}" value={formData.questionNo} placeholder="Question no" onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">Sub Question no:</label> */}
            <input type="text" name='subQuestionNo' value={formData.subQuestionNo} placeholder="Sub Question no:" onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">Sub-sub Question no:</label> */}
            <input type="text" name='partNo' value={formData.partNo} placeholder='Part no' onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">No of points:</label> */}
            <input type="text" name='noOfPoints' pattern="[0-9]{2}" value={formData.noOfPoints} placeholder='No of points' onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">Marks:</label> */}
            <input type="text" name='marks' pattern="[0-9]{3}" value={formData.marks} placeholder='Marks' onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">Keywords Marks:</label> */}
            <input type="text" name='keywordsMarks' pattern="[0-9]{3}" value={formData.keywordsMarks} placeholder='Keywords Marks' onChange={handleInputChange} className={classes}/>
          </div>
        </div>
      </div>
    </div>
  )
}

export default MakingSchemeConfigureBox
