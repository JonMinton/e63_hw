package com.codeclan.example.WhiskyTracker.controllers;

import com.codeclan.example.WhiskyTracker.models.Distillery;
import com.codeclan.example.WhiskyTracker.models.Whisky;
import com.codeclan.example.WhiskyTracker.repositories.WhiskyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class WhiskyController {

    @Autowired
    WhiskyRepository whiskyRepository;

    @GetMapping(value = "/whiskies")
    public ResponseEntity<List<Whisky>> getAllWhiskies() {
        return new ResponseEntity<>(whiskyRepository.findAll(), HttpStatus.OK);
    }

    @GetMapping(value = "/whiskies/year")
    public ResponseEntity<List<Whisky>> getWhiskeyByYear(
            @RequestParam(name = "named") int year
    ){
        return new ResponseEntity<>(whiskyRepository.findByYear(year), HttpStatus.OK);
    }



    @GetMapping(value = "/whiskies/{id}")
    public ResponseEntity getWhiskeyById(@PathVariable Long id) {
        return new ResponseEntity<>(whiskyRepository.findById(id), HttpStatus.OK);
    }

    @GetMapping(value = "/whiskies/ageanddistillery")
    public ResponseEntity<List<Whisky>> getAllWhiskiesOfAgeAndFromDistilleryId(
            @RequestParam(name="age", required = true) int age,
            @RequestParam(name="distillery_id", required = true) Long distillery_id
    ){
        return new ResponseEntity<>(whiskyRepository.findByAgeAndDistilleryId(age, distillery_id), HttpStatus.OK);
    }
//    @GetMapping(value = "/raids")
//    public ResponseEntity<List<Raid>> getAllRaidsFilterByLocation(
//            @RequestParam(name="location", required = false) String location
//    ) {
//        if (location != null){
//            return new ResponseEntity<>(raidRepository.findByLocation(location), HttpStatus.OK);
//        }
//        return new ResponseEntity<>(raidRepository.findAll(), HttpStatus.OK);
//    }
//    List<Whisky> findByAgeAndDistillery(int age, Distillery distillery);


}
