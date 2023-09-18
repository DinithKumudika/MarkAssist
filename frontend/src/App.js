import { Route, Routes } from 'react-router-dom';
import TopBar from "./Components/TopBar";
import QuestionsPage from "./Pages/QuestionsPage";
import EssayPage from './Pages/EssayPage';
import Login from './Pages/Login';
import Register from './Pages/Register';
import EmailVerifiedPage from './Pages/EmailVerifiedPage';
import TeacherPasswordChangePage from './Pages/TeacherPasswordChangePage';
import AdminDashboard from './Pages/AdminDashboard';
import SubjectsPage from './Pages/SubjectsPage';
import SubjectPage from './Pages/SubjectPage';
import YearsPage from './Pages/YearsPage';
import MarkingSchemesPage from './Pages/MarkingSchemesPage';
import MarkingSchemeConfigurePage from './Pages/MarkingSchemeConfigurePage';
import AnswerSheetsPage from './Pages/AnswerSheetsPage';
// import TopBar from './Components/TopBar';
import TeachersPage from './Pages/TeachersPage';
import MarksPage from './Pages/MarksPage';
import PapersPage from './Pages/PapersPage';
import './Components/TopBar.css';
import TeacherPage from './Pages/TeacherPage';
import TeacherPasswordChange from './Pages/TeacherPasswordChange';
import ConfigureMarks from './Pages/ConfigureMarks';
import AdminDashboard1 from './Pages/AdminDashboard1';

function App(){
  return(
    <div>
      {/* <TopBar /> */}
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        {/* <Route path="/dashboard" element={<Dashboard />} /> */}
        <Route path="/complete-registration/:token" element={<TeacherPasswordChangePage />} />
        <Route path="/verify-account/:token" element={<EmailVerifiedPage />} />

        <Route path="/essayPage" element={<EssayPage />} />

        <Route path="/subjects" element={<SubjectsPage />} />
        <Route path="/subjects/:subjectId" element={<SubjectPage />} />
        <Route path="/subjects/years/:subjectCode" element={<YearsPage />} />
        <Route path="/subjects/:year/:subjectId" element={<PapersPage />} />


        <Route path="/markingschemes" element={<SubjectsPage />} />
        <Route path="/markingschemes/years/:subjectCode" element={<YearsPage />} />
        <Route path="/markingschemes/:year/:subjectId" element={<MarkingSchemesPage />} />
         {/* <Route path="/markingschemes/:markingschemeId/:subjectId" element={<MarkingSchemeConfigurePage />} /> */}
         <Route path="/markingschemes/:subjectId" element={<MarkingSchemeConfigurePage />} />

        <Route path="/answersheets" element={<SubjectsPage />} />
        <Route path="/answersheets/years/:subjectCode" element={<YearsPage />} />
        <Route path="/answersheets/:year/:subjectId" element={<AnswerSheetsPage />} />
        <Route path="/answersheets/marks/:year/:subjectId/:paperId" element={<MarksPage />} />

        
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
        <Route path="/admin/dashboard1" element={<AdminDashboard1 />} />
        <Route path="/admin/teachers" element={<TeachersPage />} />


        <Route path="/" element={<AdminHandleStudents2 />} />
        <Route path="/adminhandleteacher2" element={<AdminHandleTeacher2 />} />
        <Route path="/adminhandlestudents" element={<AdminHandleStudents />} />

      </Routes>
    </div>
  );
}

export default App;
