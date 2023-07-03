import classnames from 'classnames'
function MakingSchemeConfigureBox({ index, formData, onChange}) {
    const handleInputChange = (event) => {
        const { name, value } = event.target;
        // console.log(name, value);
        const updatedFormData = { ...formData, [name]: value };
        // console.log(...formData);
        onChange(index, updatedFormData);
    };

    const handleSelect = () => {
        console.log("selected");
    }

    const handleDeselect = () => {
        console.log("deselected");
    }

    const classes = classnames('bg-[#EDEDED] h-10 text-center rounded rounded-lg font-bold w-full ')
    const divclasses = classnames('bg-[#EDEDED] rounded rounded-xl w-52 flex flex-row items-center justify-between mb-2 max-md:justify-between max-md:px-4 max-sm:w-48')
  return (
    <div className="flex flex-col my-6 w-full">
      <p className="font-bold mb-1">Q1</p>
      <div className=" bg-[#D4D4D4] rounded-lg flex flex-row max-sm:flex-col">
        <div className=" flex flex-row h-max  px-2 rounded-lg p-4 basis-4/5 bg-[#EDEDED] h-[100%]">
            <img  className="w-fit h-full " src="https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/uploads%2Fpdf%2F7a48e8d4-fd37-42ab-82a6-8ff1d5402cf5_cropped_2-1.jpg.jpg?alt=media" alt="Marking scheme"/>
        </div>
        <div className=" py-4 flex flex-col justify-between basis-[20%] items-center px-2 max-md:flex-col max-md:items-center">
          <div  className="w-52 max-sm:w-48 flex flex-row items-center justify-between mb-2 max-md:justify-center max-md:flex-col max-md:px-4">
            <button onClick={handleSelect} className=" font-bold text-[#191854] bg-[#EDEDED] px-2 rounded rounded-lg w-24 h-10 max-md:mb-2">Select</button>
            <button onClick={handleDeselect} className=" font-bold text-[#191854] bg-[#EDEDED] px-2 rounded rounded-lg w-24 h-10">Deselect</button>
          </div>
          <div  className={divclasses}>
            {/* <label className="mr-2">Question no:</label> */}
            <input type="text" name='question_no' pattern="[0-9]{2}" value={formData.question_no} placeholder="Question no" onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">Sub Question no:</label> */}
            <input type="text" name='sub_question_no' value={formData.sub_question_no} placeholder="Sub Question no:" onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">Sub-sub Question no:</label> */}
            <input type="text" name='sub_sub_question_no' value={formData.sub_sub_question_no} placeholder='Sub-sub Question no' onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">No of points:</label> */}
            <input type="text" name='points' pattern="[0-9]{2}" value={formData.points} placeholder='No of points' onChange={handleInputChange} className={classes}/>
          </div>
          <div className={divclasses}>
            {/* <label className="mr-2">Marks:</label> */}
            <input type="text" name='marks' pattern="[0-9]{3}" value={formData.marks} placeholder='Marks' onChange={handleInputChange} className={classes}/>
          </div>
        </div>
      </div>
    </div>
  )
}

export default MakingSchemeConfigureBox
