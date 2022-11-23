
import {BrowserRouter, Routes, Route, Link} from "react-router-dom"
import PosPos from "../modulos/pos/pages/PosPos"
import Login from "../modulos/pos/pages/Login"


const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<PosPos/>}/>
                <Route path="/login" element={<Login/>}/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router;