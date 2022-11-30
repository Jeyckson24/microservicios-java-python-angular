package com.BackendSeguridad.ms_seguridad.Repositorios;

import com.BackendSeguridad.ms_seguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioUsuario extends MongoRepository <Usuario,String> {
    @Query("{'correo':?0}")
    public Usuario findUserEmail (String correo);



}
