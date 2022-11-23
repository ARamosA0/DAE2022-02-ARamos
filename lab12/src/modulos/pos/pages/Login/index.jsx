import {
  Card,
  CardContent,
  Button,
  TextField,
  InputAdornment,
  Typography
} from "@mui/material";
import KeyIcon from "@mui/icons-material/Key";
import EmailIcon from '@mui/icons-material/Email';

import "./index.css"

const Login = () => {
  return (
    <div className="login-container">
      <Card sx={{ minWidth: 275}} >
        <CardContent sx={{background:"#0000" }} className="card-container">
          <h3>Inicio de Sesion</h3>
          <form>
            <div>
              <Typography>Email: </Typography>
              <TextField
                id="outlined-basic"
                variant="outlined"
                InputProps={{
                    startAdornment: (
                      <InputAdornment position="start">
                        <EmailIcon />
                      </InputAdornment>
                    ),
                  }}
              />
            </div>
            <div>
              <Typography sx={{marginTop:2}} >Password: </Typography>
              <TextField
                id="outlined-basic"
                variant="outlined"
                InputProps={{
                    startAdornment: (
                      <InputAdornment position="start">
                        <KeyIcon />
                      </InputAdornment>
                    ),
                  }}
              />
            </div>
            <Button sx={{marginTop:2, backgroundColor:"#ff7c30"}} fullWidth variant="contained">Iniciar Sesion</Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default Login;
