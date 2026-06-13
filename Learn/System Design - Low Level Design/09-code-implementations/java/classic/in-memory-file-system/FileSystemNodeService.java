package com.lldprep.classic.inmemoryfilesystem;

/**
 * Full reference implementation for LLD: in-memory-file-system
 * See question: 02-classic-ood/questions or matching track
 */
public class FileSystemNodeService {
    private final FileSystemNode domain;

    public FileSystemNodeService(FileSystemNode domain) {
        this.domain = domain;
    }

    public void mkdir() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}
