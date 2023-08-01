let dataTable;
let dataTableIsInitialized=false;

const dataTableOptions = {
    columnDefs:[
        {className:"centered",targets:[0,1,2,3,4]},
        {orderable:false,targets:[4]},
        {searchable:false,targets:[1,2,3]}
    ],
    pageLength: 4,
    destroy: true
};

const initDataTable=async()=>{
    if(dataTableIsInitialized){
        dataTable.destroy();
    }

    await listUsers();

    dataTable=$('#tableUsuario').DataTable({dataTableOptions});

    dataTableIsInitialized = true;
};

const listUsers = async() =>{
    try{
        const response = await fetch("http://127.0.0.1:8000/list_users/");
        const data = await response.json();

        let content=``;
        data.usuario.forEach((user, index)=>{
            content += `
                <tr>
                    <td>${index+1}</td>
                    <td>${user.nombre}</td>
                    <td>${user.apellido}</td> 
                    <td>${user.rolid_id == 1 ? '<i>Adminstrador</i>':'<i>Usuario</i>'}</td>
                    <td>
                    <button class='btn btn-sm btn-primary'>Editar</button>
                    <button class='btn btn-sm btn-danger'>Eliminar</button>
                    </td> 
                </tr>
                `;
        });
        tableBody_Usuarios.innerHTML = content;
    }catch(ex){
        alert(ex);
    }
};

window.addEventListener("load", async() => {
    await initDataTable();
});