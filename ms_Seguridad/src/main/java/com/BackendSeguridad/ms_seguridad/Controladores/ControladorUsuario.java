package com.BackendSeguridad.ms_seguridad.Controladores;

import com.BackendSeguridad.ms_seguridad.Modelos.Rol;
import com.BackendSeguridad.ms_seguridad.Modelos.Usuario;
import com.BackendSeguridad.ms_seguridad.Repositorios.RepositorioRol;
import com.BackendSeguridad.ms_seguridad.Repositorios.RepositorioUsuario;
import org.apache.logging.log4j.message.Message;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

@RestController
@RequestMapping("/user")
public class ControladorUsuario {
    @Autowired
    private RepositorioUsuario miRepositorio;
    @Autowired
    private RepositorioRol miRepoRol;
    @GetMapping("/listar")
    public List<Usuario> listar(){
        return miRepositorio.findAll();
    }
    @PostMapping("/crear")
    public Usuario crearUsuario(@RequestBody Usuario usuarioEntrada){
        usuarioEntrada.setContrasena(convertirSHA256(usuarioEntrada.getContrasena()));
        return miRepositorio.save(usuarioEntrada);
    }
    @DeleteMapping("/eliminar/{idUsuario}")
    public String eliminarUsuario(@PathVariable String idUsuario){
        miRepositorio.deleteById(idUsuario);
       return "Usuario" + idUsuario + "eliminado";
    }

    @PutMapping ("/actualizar/{idUsuario}")
    public String actualizarUsuario(@PathVariable String idUsuario, @RequestBody Usuario usuarioEntrada){
        Usuario usuarioBusqueda = miRepositorio.findById(idUsuario).orElse(null);
        usuarioBusqueda.setNombre_usuario(usuarioEntrada.getNombre_usuario());
        usuarioBusqueda.setContrasena(convertirSHA256(usuarioEntrada.getContrasena()));
        usuarioBusqueda.setCorreo(usuarioEntrada.getCorreo());
        miRepositorio.save(usuarioBusqueda);
        return "Usuario" + idUsuario + "actualizado";
    }

    @PutMapping ("/{idUsuario}/rol/{idRol}")
    public String asignarRol(@PathVariable String idUsuario, @PathVariable String idRol){

        Usuario usuarioBusqueda = miRepositorio.findById(idUsuario).orElse(null);
        Rol rolConsulta = miRepoRol.findById(idRol).orElse(null);
        usuarioBusqueda.setRol(rolConsulta);
        miRepositorio.save(usuarioBusqueda);
        return "Usuario" + idUsuario + "actualizado";
    }


    public String convertirSHA256(String password){
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e){
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for (byte b : hash){
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    @PostMapping("/login")
    public Usuario iniciarSesion (@RequestBody Usuario usuarioEntrada, HttpServletResponse codigoRespuestaHttp) throws IOException {
        String correo = usuarioEntrada.getCorreo();
        Usuario usuarioConsulta= miRepositorio.findUserEmail(correo);

        if (usuarioConsulta==null){
            System.out.println("Usuario No existe");
            codigoRespuestaHttp.sendError(HttpServletResponse.SC_UNAUTHORIZED);

            return null;
        } else {
            if (usuarioConsulta.getContrasena().equals(convertirSHA256( usuarioEntrada.getContrasena()))){
                usuarioConsulta.setContrasena(null);
                return usuarioConsulta;
            } else{
                System.out.println("contraseña Incorrecta");
                codigoRespuestaHttp.sendError(HttpServletResponse.SC_UNAUTHORIZED);
                return null;
            }

        }

    }
}
