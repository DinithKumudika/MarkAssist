import MarkAccurcyConfigureBox from "./MarkAccurcyConfigureBox";
function MarkAccurcyConfigure({marksConfigure,handleAddChild,handleRemoveChild,handleFormChange,error}) {
  //length of marksconfigure
  const length = marksConfigure.length;
  const rows = marksConfigure.map((markConfigure,index) => {
    return(
      (index!==length-1) ? 
          index===0 ? <MarkAccurcyConfigureBox handleAddChild={handleAddChild} handleRemoveChild={handleRemoveChild} index={index} key={index} data={markConfigure} handleFormChange={handleFormChange} addMinus=""/> 
          :<MarkAccurcyConfigureBox handleAddChild={handleAddChild} handleRemoveChild={handleRemoveChild} index={index} key={index} data={markConfigure} handleFormChange={handleFormChange} addMinus="-"/>
        : (markConfigure.maximum==="100") ? <MarkAccurcyConfigureBox handleAddChild={handleAddChild} handleRemoveChild={handleRemoveChild} index={index} key={index} data={markConfigure} handleFormChange={handleFormChange} addMinus="-"/>
          :<MarkAccurcyConfigureBox handleAddChild={handleAddChild} handleRemoveChild={handleRemoveChild} index={index} key={index} data={markConfigure} handleFormChange={handleFormChange} addMinus="+"/>
    )
  })
  return (
    <div className="px-10 py-4">
      {error && <div className="bg-red-500 text-white text-sm mb-2 w-full p-2 text-center mb-6">{error}</div>}
      <div className="flex flex-row justify-between text-center mb-2">
      <input disabled className="w-[150px] text-center rounded py-1 max-md:w-[60px]" type="text" value="Minimum"/>
      <input disabled className="w-[150px] text-center rounded py-1 max-md:w-[75px]" type="text" value="Maximum"/>
      <input disabled className="w-[150px] text-center rounded py-1 max-md:w-[60px]" type="text" value="Marks"/>
      <input disabled className="text-center rounded py-1 w-[36px]" type="text"/>
      </div>
      {rows}
    </div>
  )
}

export default MarkAccurcyConfigure
