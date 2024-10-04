import {
  Button,
  Icon,
  IconButton,
  TextField,
  ThemeProvider,
} from "@mui/material";
import Banner from "./Banner";
import Tag from "./Tag";
import { btn } from "../Themes";
import { useState } from "react";
import UploadPhotoBtn from "./UploadPhotoBtn";
import Grid from "./Grid";
import { ArrowForward } from "@mui/icons-material";

const LoginPage = () => {
  const [isExpandad, setIsExpanded] = useState(false);

  const login = (
    <>
      <h1>Welcome to MamaTinder!</h1>
      <TextField placeholder="Username" className="flex" />
      <TextField placeholder="Password" />
      <ThemeProvider theme={btn}>
        <Button color="secondary" variant="contained" className="w-40 ">
          Log in
        </Button>
        <Button onClick={() => expand()}>Not registered? Click here!</Button>
      </ThemeProvider>
    </>
  );

  const register = (
    <>
      <div className="flex items-center justify-between w-full bg-purple-400 bg-opacity-50">
        <div className="flex items-center">
          <img
            src="https://t4.ftcdn.net/jpg/02/66/72/41/360_F_266724172_Iy8gdKgMa7XmrhYYxLCxyhx6J7070Pr8.jpg"
            className="z-20 h-20 w-20 p-2 rounded-full"
          />
          <h1 className="ml-4">MamaTinder</h1>
        </div>
        <div className="mr-4">
          <IconButton onClick={() => shrink()} size={"large"}>
            <ArrowForward fontSize="large" />
          </IconButton>
        </div>
      </div>

      <div className="z-20 flex justify-left items-center h-4/5 w-full">
        <UploadPhotoBtn className="w-40 h-60 m-5" />
        <Grid columns={2} width={400}>
          <h1>Username:</h1>
          <TextField />
          <h1>Password:</h1>
          <TextField />
          <h1>Re-enter Password:</h1>
          <TextField />
          <h1>Birth date:</h1>
          <TextField />
        </Grid>
      </div>
    </>
  );

  const [tagContent, setTagContent] = useState(login);

  const expand = () => {
    setIsExpanded(true);
    setTimeout(() => {
      setTagContent(register);
    }, 300);
  };

  const shrink = () => {
    setIsExpanded(false);
    setTimeout(() => {
      setTagContent(login);
    }, 300);
  };

  return (
    <>
      <Banner height={"10px"} />
      <div className="flex flex-col items-center bg-purple-700 justify-center h-screen w-screen">
        <Tag isExpanded={isExpandad}>{tagContent}</Tag>
      </div>
    </>
  );
};

export default LoginPage;
