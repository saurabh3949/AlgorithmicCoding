class PeekingIterator implements Iterator<Integer> {
    Iterator<Integer> it;
    int buffer;
    boolean hasBuffer = false;
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    it = iterator;
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if (hasBuffer) return buffer;
        if (it.hasNext()) {
            buffer = it.next();
            hasBuffer = true;
            return buffer;
        } else {
            return it.next();
        }
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    if (hasBuffer) {
	        hasBuffer = false;
	        return buffer;
	    }
	    hasBuffer = false;
	    return it.next();
	}

	@Override
	public boolean hasNext() {
	    if (hasBuffer) return true;
	    return it.hasNext();
	}
}
