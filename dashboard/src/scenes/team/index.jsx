import { Box, Button, Typography, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import { mockDataTeam } from "../../data/mockData";
import { api } from "../../data/api.js";
import AdminPanelSettingsOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import IconButton from "@mui/material/IconButton";
import LockOpenOutlinedIcon from "@mui/icons-material/LockOpenOutlined";
import SecurityOutlinedIcon from "@mui/icons-material/SecurityOutlined";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import Header from "../../components/Header";
import { useState, useEffect } from 'react';
import axios from "axios";

const Team = () => {

  const [teams, setTeam] = useState([]);

  useEffect(()=>{
    fetch('http://35.208.109.101/teams')
    .then(response=>response.json())
    .then(data=>setTeam(data))
    .catch(error=>console.error('Error fetching team data:', error));
  }, []);

  const editFunction = () => {
    console.log("edit")
  }

  const deleteFunction = () => {
    console.log("delete")
  }

  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const columns = [
    { field: "id", headerName: "ID" },
    {
      field: "name",
      headerName: "Name",
      flex: 1,
      cellClassName: "name-column--cell",
      editable: true,
    },
    {
      field: "age",
      headerName: "Age",
      type: "number",
      headerAlign: "left",
      align: "left",
      editable: true,
    },
    {
      field: "phone",
      headerName: "Phone Number",
      flex: 1,
      editable: true,
    },
    {
      field: "email",
      headerName: "Email",
      flex: 1,
      editable: true,
    },
    {
      field: "accessLevel",
      headerName: "Access Level",
      flex: 1,
      renderCell: ({ row: { access } }) => {
        return (
          <Box
            width="60%"
            m="0 auto"
            p="5px"
            display="flex"
            justifyContent="center"
            backgroundColor={
              access === "admin"
                ? colors.greenAccent[600]
                : access === "manager"
                ? colors.greenAccent[700]
                : colors.greenAccent[700]
            }
            borderRadius="4px"
          >
            {access === "admin" && <AdminPanelSettingsOutlinedIcon />}
            {access === "manager" && <SecurityOutlinedIcon />}
            {access === "user" && <LockOpenOutlinedIcon />}
            <Typography color={colors.grey[100]} sx={{ ml: "5px" }}>
              {access}
            </Typography>
          </Box>
        );
      },
    },
    {
      field: "edit",
      headerName: "Edit",
      sortable: false,
      flex: 1,
      renderCell: (params) => {
        return (
          <IconButton aria-label="edit"
          variant = "contained" color="gray"
          onClick = {editFunction}
          >
            <EditIcon />
          </IconButton>
        )
      }
    },
    {
      field: "delete",
      headerName: "Delete",
      sortable: false,
      flex: 1,
      renderCell: (params) => {
        return (
          <IconButton aria-label="delete"
          variant = "contained" color="red"
          onClick = {deleteFunction}
          >
            <DeleteIcon />
          </IconButton>
        )
      }
    }
  ];

  return (
    <Box m="20px">
      <Header title="TEAM" subtitle="Managing the Team Members" />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
        }}
      >
        <DataGrid rows={teams} columns={columns} processRowUpdate={(updatedRow, originalRow) => console.log(updatedRow)} disableRowSelectionOnClick />
      </Box>
    </Box>
  );
};

export default Team;